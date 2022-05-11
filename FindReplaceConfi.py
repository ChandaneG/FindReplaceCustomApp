import configparser

def set_value_in_property_file(file_path, key, value):
    config = configparser.RawConfigParser()
    config.read(file_path)
    config.set(section,key,value)                         
    cfgfile = open(file_path,'w')
    config.write(cfgfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
    cfgfile.close()

set_value_in_property_file("C:\\Users\\chandaneg\\Desktop\\Ofline_Jobs_18_March_2020\\Italy_Temp\\job.ini","DATESTART","20170721")