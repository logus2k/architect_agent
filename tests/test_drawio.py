"""draw.io export tests — valid XML, right content, GPU-free."""
import xml.dom.minidom as minidom
from architect_agent.aspect_design import AspectDesign
from architect_agent import drawio, aspect_pipeline


def _design():
    return AspectDesign(branch="User & Access Control",
                        components=[{"name": "User"}],
                        interfaces=[{"name": "AuthenticationInterface"}],
                        consumes=[{"concern": "security"}])


def test_drawio_is_valid_xml_with_content():
    xml = drawio.aspect_drawio(_design())
    minidom.parseString(xml)  # raises if malformed
    assert "User" in xml and "AuthenticationInterface" in xml and "security" in xml
    assert "mxGraphModel" in xml and "parallelogram" in xml  # external node shape


def test_export_switches_format():
    designs = [_design()]
    m = aspect_pipeline.export_diagrams(designs, "mermaid")
    d = aspect_pipeline.export_diagrams(designs, "drawio")
    assert any(k.endswith(".mmd") for k in m)
    assert any(k.endswith(".drawio") for k in d)
    assert "flowchart" in next(iter(m.values()))
    assert "mxfile" in next(iter(d.values()))
