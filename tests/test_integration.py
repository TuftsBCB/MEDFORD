import pytest
from MEDFORD.medford import provide_args_and_go, ParserMode, OutputMode

# example error case:
# no Contributor tag -> crash

# error 1 : leading tabs are not deleted.
# error 2 : removing contributor causes it to crash.
def test_no_contributor(tmp_path) :
    example_content = "\
@MEDFORD asdf\n\
@MEDFORD-Version 2.0\n\
\n\
@Journal journal\n\
"
    
    d = tmp_path / "tmp_testfiles"
    d.mkdir()
    tmpfile = d / "only_MEDFORD.mfd"
    tmpfile.write_text(example_content, encoding="utf-8")

    provide_args_and_go(ParserMode.VALIDATE, tmpfile, OutputMode.OTHER)
    return

@pytest.mark.skip(reason="This is no longer desired functionality. Update to throw an error.")
def test_lead_spacing_ignored(tmp_path) :
    example_content = "\
        @MEDFORD asdf\n\
        @MEDFORD-Version 2.0\n\
        \n\
        @Journal journal\n\
        "
    
    d = tmp_path / "tmp_testfiles"
    d.mkdir()
    tmpfile = d / "only_MEDFORD.mfd"
    tmpfile.write_text(example_content, encoding="utf-8")

    provide_args_and_go(ParserMode.VALIDATE, tmpfile, OutputMode.OTHER)
    return