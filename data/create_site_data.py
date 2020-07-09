
import json
import os
from fetch_sheet import fetch_sheet

def build_data():
    raw_sheet = fetch_sheet()
    sheet = clean(raw_sheet)

    stats = {
        "average_score": raw_sheet[35][25],
        "median_score": raw_sheet[36][25],
        "mode_score": raw_sheet[37][25],
        "median_ppg": raw_sheet[38][25],
        "average_weight": raw_sheet[39][25],
        "median_price": raw_sheet[40][25],
        "most_common_type": raw_sheet[41][25],
        "most_common_vendor": raw_sheet[42][25],
        "most_expensive_ppg": X_expensive_ppg(sheet, is_least=False),
        "least_expensive_ppg": X_expensive_ppg(sheet, is_least=True),
        "total_weight_grams": raw_sheet[49][25],
        "most_expensive_item": raw_sheet[50][25],
        "heaviest_item":raw_sheet[51][25],
    }

    export(sheet, stats)

def X_expensive_ppg(sheet, is_least):
    ppg_index = 0
    ppg = 100.0 if is_least else 0.0
    curr_index = 0
    
    for row in sheet:
        float_price = get_float_ppg(row)
        if float_price is None:
            curr_index += 1
            continue

        if is_least:
            if float_price < ppg:
                ppg = float_price
                ppg_index = curr_index
        else:
            if float_price > ppg:
                ppg = float_price
                ppg_index = curr_index
        
        curr_index += 1

    return {"ppg": ppg, "index": ppg_index}

def get_float_ppg(raw_row):
    if raw_row[-2] == "": return None
    return float(raw_row[-2][1:])
    

def clean(sheet):
    no_empty_rows = [row for row in sheet if row[0] != '']
    truncate_rows = [row[:12] for row in no_empty_rows]
    rem_header = truncate_rows[1:]

    return rem_header


def export(sheet, stats):
    with open('teadata.json', 'w') as f:
        f.write(json.dumps(
            {
                "stats": stats,
                "raw_sheet": sheet
            }
        ))


build_data()
