def myprint(n):
    if n == 5:
        print(n)
        return 
    print(n)
    myprint(n+1)

if __name__ == "__main__":
    myprint(1)

"""
Mistake :

Don't use the default print()
Lead to recusrion depth exceeded message 
"""
