from sas7bdat import SAS7BDAT
import pandas as pd

file_names = [
    'ddf_raw',
    'dialysisaccesses',
    'dialysisaccessesinuse',
    'dialysisaccessevents',
    'facilityrounddata',
    'hospitalizations',
    'hospitalizations_raw',
    'is_f',
    'is_raw',
    'iwes_organisms_raw',
    'iwes_orgresist_raw',
    'iwes_raw',
    'iwes_treatments_raw',
    'iwp_cellcounts_raw',
    'iwp_organisms_raw',
    'iwp_orgresist_raw',
    'iwp_raw',
    'iwp_treatments_raw',
    'labs_b',
    'labs_f',
    'lrs_long',
    'lrs_raw',
    'mds',
    'mdsyr2',
    'mq_f',
    'mq_raw',
    'othermeds',
    'patientmonths',
    'patmodalityhist',
    'pd_script',
    'pet_test',
    'pqyr1',
    'questionnaires',
    'renalmeds',
    'renalmeds_raw',
    'renalmeds_text',
    'rkf_f',
    't_f',
    'ups',
    'upscorestaff',
    'upsotherstaff',
    'upsyr2',
    'upsyr2pdcathop'
]

for file_name in file_names:
    print(file_name)
    df = pd.read_sas('Phase 1/' + file_name + '.sas7bdat')
    df.to_csv('Phase 1/csv/' + file_name + '.csv', sep='\t', encoding='utf-8')
