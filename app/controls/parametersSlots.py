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



def make_slot_parameters():
    #bp.render_slots = True
    #bp.slot_length = 3
    #bp.slot_width_padding = 5
    #bp.slot_length_offset = 5
    #bp.slots_end_margin = 0

    col1, col2, col3 = st.columns(3)
    with col1:
        render_slots = st.toggle(
            "render slots",
            key="render_slots",
            value=True
        )
    with col2:
        slot_length = st.number_input(
            "length",
            key="slot_length",
            help='"length" of the slots',
            min_value=0.5, 
            max_value=150.0, 
            value=3.0,
            step=1.0
        )

    with col3:
        slot_width_padding = st.number_input(
            "width padding",
            key="slot_width_padding",
            help='"spacer width padding from the sides',
            min_value=0.0, 
            max_value=200.0, 
            value=4.0,
            step=1.0
        )

    col1, col2, col3 = st.columns(3)    
    with col1:
        slot_length_offset = st.number_input(
            "length offset",
            key="slot_length_offset",
            help='length offset between the slots',
            min_value=0.25, 
            max_value=300.00, 
            value=5.0,
            step=1.0
        )
    with col2:
        slot_end_margin = st.number_input(
            "end mrgin",
            key="slot_end_margin",
            help='Spacer margin from the ends of the walkways',
            min_value=0.0, 
            max_value=300.0, 
            value=0.0,
            step=1.0
        )

    return {
        'render_slots':render_slots,
        'slot_length':slot_length,
        'slot_width_padding':slot_width_padding,
        'slot_length_offset':slot_length_offset,
        'slot_end_margin':slot_end_margin,
    }