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

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_rails_slots = st.toggle(
            "render rails slots",
            key="render_rails_slots",
            value=True
        )
    with col2:
        rail_slot_type = st.selectbox(
            "type",
            ('archpointed', 'archround', 'box'), 
            key="rail_slot_type"
        )
    with col3:
        rail_slot_length = st.number_input(
            "length",
            key="rail_slot_length",
            help='length of the slots',
            min_value=0.25, 
            max_value=300.00, 
            value=10.0,
            step=1.0
        )
    with col4:
        rail_slot_top_padding = st.number_input(
            "top padding",
            key="rail_slot_top_padding",
            help='Padding of the slots from the top',
            min_value=0.25, 
            max_value=300.00, 
            value=6.0,
            step=1.0
        )

    col1, col2, col3 = st.columns(3) 
    with col1:
        rail_slot_length_offset = st.number_input(
            "length offset",
            key="rail_slot_length_offset",
            help='Distance between each slot',
            min_value=0.0, 
            max_value=200.0, 
            value=12.0,
            step=1.0
        )  
    with col2:
        rail_slots_end_margin = st.number_input(
            "end margin",
            key="rail_slots_end_margin",
            help='Margin from the ends',
            min_value=0.0, 
            max_value=200.0, 
            value=15.0,
            step=1.0
        )
    with col3:
        rail_slot_pointed_inner_height = st.number_input(
            "pointed inner height",
            key="rail_slot_pointed_inner_height",
            help='Height of the points',
            min_value=0.0, 
            max_value=200.0, 
            value=7.0,
            step=1.0
        )

    return {
        'render_rails_slots':render_rails_slots,
        'rail_slot_length':rail_slot_length,
        'rail_slot_top_padding':rail_slot_top_padding,
        'rail_slot_length_offset':rail_slot_length_offset,
        'rail_slots_end_margin':rail_slots_end_margin,
        'rail_slot_pointed_inner_height':rail_slot_pointed_inner_height,
        "rail_slot_type":rail_slot_type
    }