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

#--------------------  

import streamlit as st
from uuid import uuid4
import glob
from datetime import datetime
from pathlib import Path
import cadquery as cq
from cqterrain.walkway import Walkway
from controls import (
    make_sidebar, 
    make_walkway_parameters,
    make_slot_parameters,
    make_model_preview_walkway,
    make_code_view
)

def __make_tabs():
    preview_tab,walkway_tab, slot_tab, tab_code = st.tabs([
        "File Controls",
        "Walkway",
        "slots",
        "Code",
        ])
    with preview_tab:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            generate_button = st.button(f'Generate Model')
        with col2:
            export_type = st.selectbox("File type",('stl','step'), key="export_type", label_visibility="collapsed")
        with col3:
            color1 = st.color_picker(f'Model Color', '#E06600', label_visibility="collapsed", key="model_color")
        with col4:
            render = st.selectbox(f"Render", ["material", "wireframe"], label_visibility="collapsed", key="model_render")

        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_combined"
        )
    with walkway_tab:
        spool_parameters = make_walkway_parameters()

        make_model_preview_walkway(
            color1,
            render,
            export_type
        )

    with slot_tab:
        slot_parameters = make_slot_parameters()

        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_slots"
        )
    #with cradle_tab:
        #cradle_parameters = make_cradle_controls()

        #make_model_controls_cradle(
        #    color1,
        #    render,
        #    export_type
        #)
    #with cladding_tab:
        #cladding_parameters = make_cladding_controls()

        #make_model_controls_cladding(
        #    color1,
        #    render,
        #    export_type
        #)


    #combine tab parameter into one dictionary
    parameters = spool_parameters | slot_parameters #| cradle_parameters | cladding_parameters
    parameters['export_type'] = export_type

    #with tab_code:
    #    make_code_view(parameters)

    return parameters

def __initialize_session():
    if 'init' not in st.session_state:
        st.session_state['init'] = True

    if "session_id" not in st.session_state:
        st.session_state['session_id'] = uuid4()

def __generate_model(parameters):
    export_type = parameters['export_type']
    session_id = st.session_state['session_id']

    #cladding_type_param = parameters["cladding_type"]
    bp = Walkway()
    bp.length = parameters["walkway_length"]
    bp.width = parameters["walkway_width"]
    bp.height = parameters["walkway_height"]

    walkway_chamfer = parameters["walkway_chamfer"]

    if walkway_chamfer > parameters["walkway_height"]:
        walkway_chamfer = parameters["walkway_height"] - 0.00001
        st.warning('Walkway Chamfer must be less than walkway height.', icon="⚠️")

    bp.walkway_chamfer = walkway_chamfer

    bp.render_slots = parameters["render_slots"]
    bp.slot_length = 3
    bp.slot_width_padding = 5
    bp.slot_length_offset = 5
    bp.slot_width_padding = 4
    bp.slots_end_margin = 0

    bp.render_tabs = True
    bp.tab_chamfer = 4.5
    bp.tab_height = 2
    bp.tab_length = 5

    bp.render_rails = True
    bp.rail_width = 4
    bp.rail_height = 40
    bp.rail_chamfer = 28

    bp.render_rail_slots = True
    bp.rail_slot_length = 10
    bp.rail_slot_top_padding = 6
    bp.rail_slot_length_offset = 12
    bp.rail_slots_end_margin = 15
    bp.rail_slot_pointed_inner_height = 7
    bp.rail_slot_type = 'archpointed'

    bp.make()
    walkway_bridge = bp.build()

    EXPORT_NAME_SPOOL = 'model_walkway'
    cq.exporters.export(walkway_bridge,f'{EXPORT_NAME_SPOOL}.{export_type}')
    cq.exporters.export(walkway_bridge,'app/static/'+f'{EXPORT_NAME_SPOOL}_{session_id}.stl')


def __make_app():
    if st.session_state['init']:
        with st.spinner('Starting Application..'):
            model_parameters = {
                'walkway_length': 225.0,
                'walkway_width': 75.0,
                'walkway_height': 6.0, 
                'walkway_chamfer':3,
                'render_slots':True,
                #'spool_radius': 97.5, 
                #'spool_cut_radius': 36.5, 
                #'spool_wall_width': 4.0, 
                #'spool_internal_wall_width': 3.0, 
                #'spool_internal_z_translate': 0.0, 
                #'cradle_length': 150.0, 
                #'cradle_width': 75.0, 
                #'cradle_height': 63.0, 
                #'cradle_angle': 45.0, 
                #'cladding_type':'plain',
                #'cladding_seed':'power!',
                #'cladding_count': 17, 
                #'clading_width': 33.0, 
                #'cladding_height': 5.0, 
                #'cladding_inset': 5.0,
                'export_type':'stl'
            }

            __generate_model(model_parameters)
            model_parameters = __make_tabs()
            st.session_state['init'] = False
    else:
        with st.spinner('Generating Model..'):
            __generate_model(st.session_state)
            model_parameters = __make_tabs()
            
    #st.write(st.session_state)


def __clean_up_static_files():
    files = glob.glob("app/static/model_*.stl")
    today = datetime.today()
    #print(files)
    for file_name in files:
        file_path = Path(file_name)
        modified = file_path.stat().st_mtime
        modified_date = datetime.fromtimestamp(modified)
        delta = today - modified_date
        #print('total seconds '+str(delta.total_seconds()))
        if delta.total_seconds() > 1200: # 20 minutes
            #print('removing '+file_name)
            file_path.unlink()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Walkway Generator",
        page_icon="🧊"
    )
    __initialize_session()
    __make_app()
    make_sidebar()
    __clean_up_static_files()