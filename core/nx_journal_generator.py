def generate_nx_journal(stats):

    code = f'''
import NXOpen

def main():

    theSession = NXOpen.Session.GetSession()

    lw = theSession.ListingWindow
    lw.Open()

    lw.WriteLine("Reverse CAD Analysis")

    lw.WriteLine("Volume: {stats['Volume_mm3']} mm3")
    lw.WriteLine("Surface Area: {stats['Surface_Area_mm2']} mm2")

if __name__ == "__main__":
    main()
'''

    return code