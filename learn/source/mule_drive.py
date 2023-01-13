"""
to cope with excel file for mule drive BCI script
find ScriptName in sheet Master_Asic
then only retain script name, i.e. last str after '/',
write res to a txt.
"""
import xlrd


def get_script_name_from_whole_path(name=''):
    return name.split('/')[-1]


def get_test_plan_sheet(sheets):
    """
    get_test_plan_sheet
    """
    for item in sheets:
        if item.name.endswith("Master_ASIC"):
            return item
        if item.name.endswith("Master_Matrix_Gensim"):
            return item
    raise Exception("No test plan sheet found")


def load_excel(fpath):
    """
    load_excel
    """
    sheets = None
    try:
        with xlrd.open_workbook(fpath) as excl:
            sheets = excl.sheets()
    except Exception as str_err:  # pylint: disable=W0703
        print(str(str_err))
    return sheets


def get_key_cols(target_sheet):
    """
    get_key_cols
    """
    res = {
        "Module": None,
        "ScriptName": None,
        "TAG": None,
        "ScriptPath": None,
        "SpecificParameter": None,
        "MRT": None,
        "BCI": None,
        "Exclude_Customer": None,
    }

    for col in range(target_sheet.ncols):
        val = target_sheet.cell_value(rowx=0, colx=col)
        if val in list(res.keys()):
            print(val)
            print(col)
            res[val] = col
    return res


class ModifyExcel(object):
    """
    class ModifyExcel
    """

    def __init__(self):
        self.test_plan_path = '/users/ssdrive/tmp/Test_Plan.xlsx'
        self.test_plan_sheet = get_test_plan_sheet(load_excel(self.test_plan_path))

    def modify_script_name(self):
        """
        modify_script_name
        """
        with open('tmp_res.txt', 'w') as f:
            key_cols = get_key_cols(self.test_plan_sheet)
            for row in range(2, self.test_plan_sheet.nrows):
                script = self.test_plan_sheet.cell_value(rowx=row, colx=key_cols["ScriptName"])
                new = get_script_name_from_whole_path(script)
                f.writelines(new + '\n')


if __name__ == '__main__':
    m = ModifyExcel()
    m.modify_script_name()
