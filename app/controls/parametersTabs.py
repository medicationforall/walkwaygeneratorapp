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



def make_tab_parameters():
    #bp.tab_chamfer = 4.5
    #bp.tab_height = 2
    #bp.tab_length = 5

    col1, col2, col3 = st.columns(3)
    with col1:
        render_tabs = st.toggle(
            "render tabs",
            key="render_tabs",
            value=True
        )
    with col2:
        tab_length = st.number_input(
            "tab length",
            key="tab_length",
            help='length of the tab',
            min_value=0.25, 
            max_value=300.00, 
            value=5.0,
            step=1.0
        )
    with col3:
        tab_height = st.number_input(
            "height",
            key="tab_height",
            help='Height of the tabs',
            min_value=0.5, 
            max_value=200.0, 
            value=2.0,
            step=1.0
        )

    col1, col2, col3 = st.columns(3)    
    with col1:
        tab_chamfer = st.number_input(
            "chamfer",
            key="tab_chamfer",
            help='Corner chamfer on the the tabs',
            min_value=0.5, 
            max_value=150.0, 
            value=4.5,
            step=1.0
        )

    return {
        'render_tabs':render_tabs,
        'tab_chamfer':tab_chamfer,
        'tab_height':tab_height,
        'tab_length':tab_length
    }