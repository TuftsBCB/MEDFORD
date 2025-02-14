from typing import Any, Dict, List, Tuple

import pytest

from MEDFORD.models.generics import Contributor, Entity
from MEDFORD.objs.dictionizer import Dictionizer as D
from MEDFORD.objs.linecollections import Block
from MEDFORD.objs.linecollector import LineCollector as LC
from MEDFORD.objs.linereader import LineReader as LR
from MEDFORD.objs.lines import Line


class TestPydanticModels:
    def setup_method(self, test_method):
        pass

    def preprocess_lines(self, lines: List[str]) -> Tuple[List[Block], Dict[str, Any]]:
        line_objs: List[Line] = []
        for idx, l in enumerate(lines):
            # TODO : shouldn't have to manually be getting rid of None lines tbh
            pl = LR.process_line(l, idx)
            if pl is not None:
                line_objs.append(pl)

        lc = LC(line_objs)
        bls = lc.get_flat_blocks()
        d = D(lc.defined_macros, lc.get_1lvl_blocks())
        return (bls, d.generate_dict(bls))

    @pytest.mark.skip(reason="block has no attribute headDetail")
    def test_contributor(self):
        sample_lines = ["@Contributor Polina Shpilker"]

        (bls, cd) = self.preprocess_lines(sample_lines)
        contributor_data = cd["Contributor"][0]

        res = Contributor(**contributor_data)

        assert res.name[1] == "Polina Shpilker"
        assert res.name[0] == bls[0].headDetail
        assert res.Block == bls[0]

    @pytest.mark.skip(reason="pydantic validation fails")
    def test_entity(self):
        sample_lines = ["@Contributor Polina Shpilker"]

        (bls, cd) = self.preprocess_lines(sample_lines)
        contributor_data = cd

        _ = Entity(**contributor_data)
        # TODO : finish test
