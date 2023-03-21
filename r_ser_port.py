import fct_def

sensor_save = fct_def.readserport_mkr_mega()

fsave = input("file speichern?")
if "y" in fsave:
    fct_def.writefile(sensor_save)
