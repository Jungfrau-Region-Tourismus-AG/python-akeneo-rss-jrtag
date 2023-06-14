from extract import extract
#from transform import transform, transformAkeneotoMasch
#from load import load

def __main__():
  print("STARTING")
  print("EXTRACTING")
  extractData = extract()
  print(extractData)
  print("TRANSFORMING")
  #transformDataAkeneo = transformAkeneotoMasch(extractDataAkeneo)
  #transformData = transform(extractData, transformDataAkeneo)
  
  print("LOADING")
  #loadData = load(transformData)

  print("FINISHED")

if __name__== "__main__":
    __main__()