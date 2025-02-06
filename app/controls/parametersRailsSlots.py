# Copyright 2025 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

def make_rails_slots_parameters():
    #bp.render_rail_slots = True
    #bp.rail_slot_length = 10
    #bp.rail_slot_top_padding = 6
    #bp.rail_slot_length_offset = 12
    #bp.rail_slots_end_margin = 15
    #bp.rail_slot_pointed_inner_height = 7
    #bp.rail_slot_type = 'archpointed'

    col1, col2, col3 = st.columns(3)
    with col1:
        render_rails_slots = st.toggle(
            "render rails slots",
            key="render_rails_slots",
            value=True
        )
    #with col2:
    #    rail_width = st.number_input(
    #        "width",
    #        key="rail_width",
    #        help='width of the rails',
    #        min_value=0.25, 
    #        max_value=300.00, 
    #        value=4.0,
    #        step=1.0
    #    )
    #with col3:
    #    rail_height = st.number_input(
    #        "height",
    #        key="rail_height",
    #        help='Height of the rails',
    #        min_value=0.25, 
    #        max_value=300.00, 
    #        value=40.0,
    #        step=1.0
    #    )


    #col1, col2, col3 = st.columns(3)    
    #with col1:
    #    rail_chamfer = st.number_input(
    #        "chamfer",
    #        key="rail_chamfer",
    ##        help='Chamfer of the rails',
    #        min_value=0.0, 
    #        max_value=200.0, 
    #        value=28.0,
    #        step=1.0
    #    )

    return {
        'render_rails_slots':render_rails_slots,
        #'rail_width':rail_width,
        #'rail_height':rail_height,
        #'rail_chamfer':rail_chamfer,
    }