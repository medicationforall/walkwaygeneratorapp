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
    make_tab_parameters,
    make_rails_parameters,
    make_rails_slots_parameters,
    make_model_preview_walkway,
    make_code_view
)

def __make_tabs():
    preview_tab,walkway_tab, slot_tab, rails_tab, rails_slots_tab, tab_tab, tab_code = st.tabs([
        "File Controls",
        "Walkway",
        "Slots",
        "Rails",
        "Rail Slots",
        "Tabs",
        "Code",
        ])
    with preview_tab:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            generate_button = st.button(f'Generate Model')
        with col2:
            export_type = st.selectbox("File type",('stl','step'), key="export_type", label_visibility="collapsed")
        with col3:
            color1 = st.color_picker(f'Model Color', '#E06600', label_visibility="collapsed", key="model_color")
        with col4:
            render = st.selectbox(f"Render", ["material", "wireframe"], label_visibility="collapsed", key="model_render")
        with col5:
            auto_rotate_control = st.toggle('Auto Rotate',key="auto_rotaate",value=True)

        auto_rotate = 'true' if auto_rotate_control else 'false'
        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_combined",
            auto_rotate
        )
    with walkway_tab:
        spool_parameters = make_walkway_parameters()

        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_alkway",
            auto_rotate
        )

    with slot_tab:
        slot_parameters = make_slot_parameters()

        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_slots",
            auto_rotate
        )

    with tab_tab:
        tab_parameters = make_tab_parameters()
    
        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_tabs",
            auto_rotate
        )

    
    with rails_tab:
        rails_parameters = make_rails_parameters()
    
        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_rails",
            auto_rotate
        )

    with rails_slots_tab:
        rails_slots_parameters = make_rails_slots_parameters()
    
        make_model_preview_walkway(
            color1,
            render,
            export_type,
            "model_preview_rails_slots",
            auto_rotate
        )


    #combine tab parameter into one dictionary
    parameters:dict = spool_parameters | slot_parameters | tab_parameters | rails_parameters | rails_slots_parameters
    parameters['export_type'] = export_type

    with tab_code:
        make_code_view(parameters)

    return parameters

def __initialize_session():
    if 'init' not in st.session_state:
        st.session_state['init'] = True

    if "session_id" not in st.session_state:
        st.session_state['session_id'] = uuid4()


def __make_app():
    if st.session_state['init']:
        with st.spinner('Starting Application..'):
            model_parameters = {
                'walkway_length': 225.0,
                'walkway_width': 75.0,
                'walkway_height': 6.0, 
                'walkway_chamfer':3,
                'render_slots':True,
                'slot_length':3,
                'slot_width_padding':5,
                'slot_length_offset':5,
                'slot_end_margin':0,
                'render_tabs':True,
                'tab_chamfer':4.5,
                'tab_height':2,
                'tab_length':5,
                'render_rails':True,
                'rail_width':4,
                'rail_height':40,
                'rail_chamfer':28,
                'render_rails_slots':True,
                'rail_slot_length':10,
                'rail_slot_top_padding':6,
                'rail_slot_length_offset':12,
                'rail_slots_end_margin':15,
                'rail_slot_pointed_inner_height':7,
                'rail_slot_type':'archpointed',
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

def __calculate_chamfer(parameters:dict,chamfer:str,check:str):
    calulated_chamfer = parameters[chamfer]
    if calulated_chamfer >= parameters[check]:
        calulated_chamfer = parameters[check] - 0.00001
        chamfer_str = chamfer.replace('_',' ')
        check_str = check.replace('_',' ')
        st.warning(f'{chamfer_str} {parameters[chamfer]} must be less than {check_str} {parameters[check]}.', icon="⚠️")
    #elif divide_by_two and calulated_chamfer >= (parameters[check])/2:
    #    calulated_chamfer = 1
    #    chamfer_str = chamfer.replace('_',' ')
    #    check_str = check.replace('_',' ')
    #    st.warning(f'{chamfer_str} {parameters[chamfer]} must be less than {check_str} divided by two {parameters[check]/2}.', icon="⚠️")
    return calulated_chamfer

def __generate_model(parameters):
    export_type = parameters['export_type']
    session_id = st.session_state['session_id']

    #cladding_type_param = parameters["cladding_type"]
    bp = Walkway()
    bp.length = parameters["walkway_length"]
    bp.width = parameters["walkway_width"]
    bp.height = parameters["walkway_height"]

    walkway_chamfer = __calculate_chamfer(parameters,"walkway_chamfer", "walkway_height")
    bp.walkway_chamfer = walkway_chamfer

    bp.render_slots = parameters["render_slots"]
    bp.slot_length = parameters["slot_length"]
    bp.slot_width_padding = parameters["slot_width_padding"]
    bp.slot_length_offset = parameters["slot_length_offset"]
    bp.slots_end_margin = parameters["slot_end_margin"]

    bp.render_tabs = parameters["render_tabs"]

    tab_chamfer = __calculate_chamfer(parameters,"tab_chamfer", "tab_length")
    bp.tab_chamfer = tab_chamfer
    bp.tab_height = parameters["tab_height"]
    bp.tab_length = parameters["tab_length"]

    bp.render_rails = parameters["render_rails"]
    bp.rail_width = parameters['rail_width']
    bp.rail_height = parameters['rail_height']

    rail_chamfer = __calculate_chamfer(parameters,"rail_chamfer", "rail_height")

    if rail_chamfer >= parameters["walkway_length"]/2:
        rail_chamfer = parameters["walkway_length"]/2 - 0.00001
        chamfer_str = "rail_chamfer".replace('_',' ')
        check_str = "walkway_length".replace('_',' ')
        st.warning(f'{chamfer_str} {parameters["rail_chamfer"]} must be less than half of {check_str} {parameters["walkway_length"]/2} {rail_chamfer}.', icon="⚠️")

    bp.rail_chamfer = rail_chamfer

    bp.render_rail_slots = parameters['render_rails_slots']
    bp.rail_slot_length = parameters['rail_slot_length']
    bp.rail_slot_top_padding = parameters['rail_slot_top_padding']
    bp.rail_slot_length_offset = parameters['rail_slot_length_offset']
    bp.rail_slots_end_margin = parameters['rail_slots_end_margin']
    bp.rail_slot_pointed_inner_height = parameters['rail_slot_pointed_inner_height']
    bp.rail_slot_type = parameters['rail_slot_type']

    bp.make()
    walkway_bridge = bp.build()

    EXPORT_NAME_SPOOL = 'model_walkway'
    cq.exporters.export(walkway_bridge,f'{EXPORT_NAME_SPOOL}.{export_type}')
    cq.exporters.export(walkway_bridge,'app/static/'+f'{EXPORT_NAME_SPOOL}_{session_id}.stl')

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