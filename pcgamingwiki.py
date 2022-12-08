import pypcgamingwiki as P 
import os
import sys as S
import returnpath as R

dirname = R.dir()
print(dirname)

def main():
	try:
		G = P.Browser(S.argv[1], dirname) 
		page = G.search()
		val = G.parse(page)
		pagedata = G.write(val)
	except:
		G = P.Browser(input("Enter game name: "), dirname)
		page = G.search() 
		val = G.parse(page)
		pagedata = G.write(val)

if __name__ == "__main__":
    S.exit(main())
