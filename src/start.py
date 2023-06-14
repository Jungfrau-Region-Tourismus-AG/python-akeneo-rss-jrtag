from extract import extract
from transform import transform
#from load import load

def __main__():
  print("STARTING")
  ## EXTRACTING
  print("EXTRACTING")
  extractData = extract()
  #print(extractData)

  ## TRANSFORMING
  print("TRANSFORMING")
  #transformDataAkeneo = transformAkeneotoMasch(extractDataAkeneo)
  transformData = transform(extractData)
  print(transformData)

  ## LOADING
  print("LOADING")
  #loadData = load(transformData)

  print("FINISHED")

if __name__== "__main__":
    __main__()