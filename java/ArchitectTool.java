import org.omg.sysml.interactive.SysMLInteractive;
import org.omg.sysml.interactive.SysMLInteractiveResult;
import org.omg.sysml.plantuml.SysML2PlantUMLSvc;
import org.omg.sysml.plantuml.SysML2PlantUMLLinkProvider;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.xtext.validation.Issue;
import net.sourceforge.plantuml.SourceStringReader;
import net.sourceforge.plantuml.FileFormat;
import net.sourceforge.plantuml.FileFormatOption;

import java.io.FileOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * Headless SysML v2 validation and diagram rendering for the Architect Agent.
 *
 *   java -cp <kernel.jar>:. ArchitectTool <library-dir> <model.sysml> [out.png]
 *
 * The library directory MUST be absolute: loadLibrary() concatenates hardcoded
 * subdirectory names containing spaces ("Kernel Libraries"), and with a relative
 * path EMF URI-encodes them and then fails to decode, yielding
 * FileNotFoundException on .../Kernel%20Libraries/... . Do not "fix" this by
 * renaming the directories — the names are constants, and renaming makes
 * loadLibrary read zero files while still appearing to succeed.
 *
 * Emits a single JSON object on stdout. Exit 0 = valid, 1 = invalid, 2 = usage.
 */
public class ArchitectTool {

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.out.println("{\"error\":\"usage: ArchitectTool <library-dir> <model.sysml> [out.png]\"}");
            System.exit(2);
        }
        Path libDir = Path.of(args[0]).toAbsolutePath();
        String source = Files.readString(Path.of(args[1]));
        String outPng = args.length > 2 ? args[2] : null;

        SysMLInteractive si = SysMLInteractive.getInstance();
        si.loadLibrary(libDir.toString());

        SysMLInteractiveResult result = si.process(source);
        if (result.getException() != null) {
            System.out.println("{\"valid\":false,\"exception\":" + quote(result.formatException()) + "}");
            System.exit(1);
        }

        StringBuilder json = new StringBuilder("{");
        json.append("\"valid\":").append(!result.hasErrors());
        json.append(",\"syntax_errors\":").append(issues(result.getSyntaxErrors()));
        json.append(",\"semantic_errors\":").append(issues(result.getSemanticErrors()));
        json.append(",\"warnings\":").append(issues(result.getWarnings()));

        // Rendering only happens for a valid model — an invalid one cannot be
        // resolved into PlantUML, and drawing an unvalidated model is pointless.
        if (outPng != null && !result.hasErrors()) {
            try {
                String puml = plantUml(result.getRootElement());
                // Smetana is PlantUML's pure-Java layout engine. Without this pragma
                // PlantUML shells out to GraphViz `dot`, which we do not ship.
                String withSmetana = puml.replaceFirst("(?m)^@startuml.*$", "$0\n!pragma layout smetana");
                Files.writeString(Path.of(outPng + ".puml"), withSmetana);
                try (FileOutputStream out = new FileOutputStream(outPng)) {
                    new SourceStringReader(withSmetana)
                        .outputImage(out, new FileFormatOption(FileFormat.PNG));
                }
                json.append(",\"png\":").append(quote(outPng));
                json.append(",\"puml\":").append(quote(outPng + ".puml"));
            } catch (Exception e) {
                // A render failure is non-fatal: the model is already known good.
                json.append(",\"render_error\":").append(quote(String.valueOf(e.getMessage())));
            }
        }
        json.append("}");
        System.out.println(json);
        System.exit(result.hasErrors() ? 1 : 0);
    }

    private static String plantUml(EObject root) {
        SysML2PlantUMLSvc svc = new SysML2PlantUMLSvc(new SysML2PlantUMLLinkProvider() {
            public String getLinkString(EObject e) { return null; }
            public String getText(EObject e) { return null; }
        });
        return svc.getPlantUMLCode(List.of(root), List.of());
    }

    private static String issues(List<Issue> issues) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < issues.size(); i++) {
            Issue it = issues.get(i);
            if (i > 0) sb.append(",");
            sb.append("{\"message\":").append(quote(it.getMessage()))
              .append(",\"line\":").append(it.getLineNumber())
              .append(",\"column\":").append(it.getColumn()).append("}");
        }
        return sb.append("]").toString();
    }

    private static String quote(String s) {
        if (s == null) return "null";
        StringBuilder sb = new StringBuilder("\"");
        for (char c : s.toCharArray()) {
            switch (c) {
                case '"':  sb.append("\\\""); break;
                case '\\': sb.append("\\\\"); break;
                case '\n': sb.append("\\n");  break;
                case '\r': sb.append("\\r");  break;
                case '\t': sb.append("\\t");  break;
                default:
                    if (c < 0x20) sb.append(String.format("\\u%04x", (int) c));
                    else sb.append(c);
            }
        }
        return sb.append("\"").toString();
    }
}
