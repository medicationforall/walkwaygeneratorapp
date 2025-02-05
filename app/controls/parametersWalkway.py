# Copyright 2023 James Adams
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

def make_walkway_parameters():
    col1, col2, col3 = st.columns(3)
    with col1:
        walkway_length = st.number_input(
            "length",
            key="walkway_length",
            help='"Length" of the walkway',
            min_value=10.0, 
            max_value=500.0, 
            value=225.0,
            step=1.0
        )

    with col2:
        walkway_width = st.number_input(
            "width",
            key="walkway_width",
            help='"Width" of the walkway',
            min_value=10.0, 
            max_value=500.0, 
            value=75.0,
            step=1.0
        )

    with col3:
        walkway_height = st.number_input(
            "height",
            key="walkway_height",
            help='"Height" of the walkway',
            min_value=1.0, 
            max_value=300.0, 
            value=6.0 ,
            step=1.0
        )

    col1, col2, col3 = st.columns(3)    
    with col1:
        walkway_chamfer = st.number_input(
            "Chamfer",
            key="walkway_chamfer",
            help='Must be less than Height',
            min_value=0.25, 
            max_value=100.00, 
            value=3.0,
            step=0.25
        )
    #with col2:
    #    spool_internal_wall_width = st.number_input(
    #        "internal width",
    #        key="spool_internal_wall_width",
    #        min_value=1.0, 
    #        max_value=100.0, 
    #        value=3.0,
    #        step=1.0
    #    )
    #with col3:
    #    spool_internal_z_translate = st.number_input(
    #        "z translate",
    #        key="spool_internal_z_translate",
    #        min_value=-100.0, 
    ##        max_value=100.0, 
    #        value=0.0,
    #        step=1.0
    #    )


    return {
        'walkway_length':walkway_length,
        'walkway_width':walkway_width,
        'walkway_height':walkway_height,
        'walkway_chamfer':walkway_chamfer
        #'spool_radius':spool_radius,
        #'spool_cut_radius':spool_cut_radius,
        #'spool_wall_width':spool_wall_width,
        #'spool_internal_wall_width':spool_internal_wall_width,
        #'spool_internal_z_translate':spool_internal_z_translate
    }