import random

# ________________________________________________________________________________________________________
# X Hospital Find Nearest Hospital 

def alkapuri_best_clinic() :
     print("Here is Best Clinic in Alkapuri Area")
     try : 
      option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Shraddha Clinic \n2.)Shree Clinic \n3.)patel Clinic\nYour Choice : ").strip()
      while True :
            if option == "1" :
                 print("You Have Selected Shraddha Clinic \nDoctor Name : Dr.Misthi \nAddress : 23, Alkapuri, Near New Bridge Vadodara, Gujarat 390007 \nContact No : +91 98765 43210")
                 break
            elif option == "2" :
                 print("You Have Selected Shree Clinic \nDoctor Name : Dr.Aadarsh \nAddress : 45, Alkapuri, 1st floor, Shashwat Complex, Vadodara, Gujarat 390007 \nContact No : +91 87654 32109")
                 break
            elif option == "3" :
                 print("You Have Selected Patel Clinic \n Doctor Name : Dr.Divyang Rathva \nAddress : 67, Alkapuri, Near Laxmi Society Vadodara, Gujarat 390007 \nContact No : +91 76543 21098")
                 break
            else :
                 option = input("Please Enter Valid Option For Hospital ✔ ").strip()
     except Exception as e :
          print("Please Enter Valid Option")



def gotri_best_clinic() :
        print("Here is Best Clinic in Gotri Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Manav Clinic \n2.)Shivam Clinic \n3.)Rathod Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Manav Clinic \nDoctor Name : Dr.Aakash \nAddress : 23, Gotri, Near New Bridge Vadodara, Gujarat 390021 \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Shivam Clinic \nDoctor Name : Dr.Krishna Patel \nAddress : 89, Gotri Road, Near Gotri Circle Vadodara, Gujarat 390021 \nContact No : +91 65432 10987")
                    break
                elif option == "3" :
                    print("You Have Selected Rathod Clinic \n Doctor Name : Dr.Hardik Rathod \nAddress : 12, Gotri Main Road, Near Gotri Bus Stand Vadodara, Gujarat 390021 \nContact No : +91 54321 09876")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")


def manjalpur_best_clinic() :
        print("Here is Best Clinic in Manjalpur Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Nidhi Clinic \n2.)Kumar Clinic \n3.)Shah Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Nidhi Clinic \nDoctor Name : Dr.Nidhi \nAddress : 56, Manjalpur, Near Manjalpur Circle Vadodara, Gujarat 390011 \nContact No : +91 98765 43210")
                    
                elif option == "2" :
                    print("You Have Selected Kumar Clinic \nDoctor Name : Dr.Rajesh Kumar \nAddress : 78, Manjalpur Main Road, Near Manjalpur Bus Stand Vadodara, Gujarat 390011 \nContact No : +91 87654 32109")
                  
                elif option == "3" :
                    print("You Have Selected Shah Clinic \n Doctor Name : Dr.Meena Shah \nAddress : 90, Manjalpur, Near Manjalpur Bus Stand Vadodara, Gujarat 390011 \nContact No : +91 76543 21098")
                    break
        except Exception as e :
            print("Please Enter Valid Option")


def navrang_pura_best_clinic() :
     print("Here is Best Clinic in Navrangpura Area")
     try : 
      option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Apollo Clinic \n2.)Shree nath Clinic \n3.)poojaClinic\nYour Choice : ").strip()
      while True :
            if option == "1" :
                 print("You Have Selected Apollo Clinic \nDoctor Name : Dr.Sheikh \nAddress : 23, Navrangpura, Near New Bridge Ahemdabad, Gujarat 390007 \nContact No : +91 98765 43210")
                 break
            elif option == "2" :
                 print("You Have Selected Shree nath Clinic \nDoctor Name : Dr.Aadarsh \nAddress : 45, Navrangpura, 1st floor, Shashwat Complex, Ahemdabad, Gujarat 390007 \nContact No : +91 87654 32109")
                 break
            elif option == "3" :
                 print("You Have Selected Pooja Clinic \n Doctor Name : Dr.Divyang Rathva \nAddress : 67, Navrangpura, Near Laxmi Society Ahemdabad, Gujarat 390007 \nContact No : +91 76543 21098")
                 break
            else :
                 option = input("Please Enter Valid Option For Hospital ✔ ").strip()
     except Exception as e :
          print("Please Enter Valid Option")


def paldi_best_clinic() :
        print("Here is Best Clinic in Paldi Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Bharat Clinic \n2.)Space Clinic \n3.)raksha Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Bharat Clinic \nDoctor Name : Dr.Bharat \nAddress : 23, Paldi, Near New Bridge Ahemdabad, Gujarat 390021 \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Space Clinic \nDoctor Name : Dr.Rohit \nAddress : 89, Paldi Road, Near Gotri Circle Ahemdabad, Gujarat 390021 \nContact No : +91 65432 10987")
                    break
                elif option == "3" :
                    print("You Have Selected Raksha Clinic \n Doctor Name : Dr.Axar \nAddress : 12, Paldi Main Road, Near Gotri Bus Stand Ahemdabad, Gujarat 390021 \nContact No : +91 54321 09876")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")


def vasatrapur_best_clinic() :
        print("Here is Best Clinic in Vastrapur Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Jeevan Clinic \n2.)Rakesh Clinic \n3.)Baba Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Jeevan Clinic \nDoctor Name : Dr.Harsh \nAddress : 23, Vastrapur, Near New Bridge Ahemdabad, Gujarat 390015 \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Rakesh Clinic \nDoctor Name : Dr.Mohini \nAddress : 89, Vastrapur Road, Near Gotri Circle Ahemdabad, Gujarat 390015 \nContact No : +91 65432 10987")
                    break
                elif option == "3" :
                    print("You Have Selected Baba Clinic \n Doctor Name : Dr.Rakesh \nAddress : 12, Vastrapur Main Road, Near Gotri Bus Stand Ahemdabad, Gujarat 390015 \nContact No : +91 54321 09876")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")



def adajan_best_Clinic() :
        print("Here is Best Clinic in Adajan Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Shraddha Clinic \n2.)Shree Clinic \n3.)patel Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Shraddha Clinic \nDoctor Name : Dr.Misthi \nAddress : 23, Adajan, Near New Bridge Surat, Gujarat 390007 \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Shree Clinic \nDoctor Name : Dr.Aadarsh \nAddress : 45, Adajan, 1st floor, Shashwat Complex, Surat, Gujarat 390007 \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Patel Clinic \n Doctor Name : Dr.Divyang Rathva \nAddress : 67, Adajan, Near Laxmi Society Surat, Gujarat 390007 \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")



def udhna_best_Clinic() :
        print("Here is Best Clinic in Udhna Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Manav Clinic \n2.)Shivam Clinic \n3.)Rathod Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Manav Clinic \nDoctor Name : Dr.Dhaval \nAddress : 23, Udhna, Near New Bridge Surat, Gujarat 390021 \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Shivam Clinic \nDoctor Name : Dr.Shrushti Patal \nAddress : 89, Udhna Road, Near  Circle Surat, Gujarat 390021 \nContact No : +91 65432 10987")
                    break
                elif option == "3" :
                    print("You Have Selected Rathod Clinic \n Doctor Name : Dr.Mitesh Suthariya\nAddress : 12, Udhna Main Road, Near Bus Stand Surat, Gujarat 390021 \nContact No : +91 54321 09876")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")


def varachha_best_Clinic() :
        print("Here is Best Clinic in Varachha Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Nidhi Clinic \n2.)Kumar Clinic \n3.)Shah Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Nidhi Clinic \nDoctor Name : Dr.Nidhi \nAddress : 56, Varachha, Near  Circle Surat, Gujarat 390011 \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Kumar Clinic \nDoctor Name : Dr.Rajesh Kumar \nAddress : 78, Varachha Main Road, Near  Bus Stand Surat, Gujarat 390011 \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Shah Clinic \n Doctor Name : Dr.Meena Shah \nAddress : 90, Varachha, Near  Bus Stand Surat, Gujarat 390011 \nContact No : +91 76543 21098")
                    break
        except Exception as e :
            print("Please Enter Valid Option")


def andheri_best_Clinic() :
     print("Here is Best Clinic in Andheri Area")
     try : 
      option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Apollo Clinic \n2.)Shree nath Clinic \n3.)poojaClinic\nYour Choice : ").strip()
      while True :
            if option == "1" :
                 print("You Have Selected Apollo Clinic \nDoctor Name : Dr.Sheikh \nAddress : 23, Andheri, Near New Bridge Andheri Maharashtra  \nContact No : +91 98765 43210")
                 break
            elif option == "2" :
                 print("You Have Selected Shree nath Clinic \nDoctor Name : Dr.Aadarsh \nAddress : 45, Andheri, 1st floor, Shashwat Complex, Andheri Maharashtra  \nContact No : +91 87654 32109")
                 break
            elif option == "3" :
                 print("You Have Selected Pooja Clinic \n Doctor Name : Dr.Divyang Rathva \nAddress : 67, Andheri, Near Laxmi Society,Andheri Maharashtra\nContact No : +91 76543 21098")
                 break
            else :
                 option = input("Please Enter Valid Option For Hospital ✔ ").strip()
     except Exception as e :
          print("Please Enter Valid Option")

def bandra_best_Clinic() :
        print("Here is Best Clinic in Bandra Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Bharat Clinic \n2.)Space Clinic \n3.)raksha Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Bharat Clinic \nDoctor Name : Dr.Bharat \nAddress : 23, Bandra, Near New Bridge, Bandra Maharashtra \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Space Clinic \nDoctor Name : Dr.Rohit \nAddress : 89, Bandra Road, Near  Circle ,Bandra Maharashtra\nContact No : +91 65432 10987")
                    break
                elif option == "3" :
                    print("You Have Selected Raksha Clinic \n Doctor Name : Dr.Axar \nAddress : 12, Bandra Main Road, Near Bus Stand ,Bandra Maharashtra\nContact No : +91 98549 09876")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")
def dadar_best_Clinic() :
        print("Here is Best Clinic in Dadar Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)pushti Clinic \n2.)patel Clinic \n3.)Shah Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Pushti Clinic \nDoctor Name : Dr.Pushti \nAddress : 56, Dadar, Near  Circle Vadodara, Maharastra \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Patel Clinic \nDoctor Name : Dr.Patel \nAddress : 78, Dadar, Near Bus Stand  Bandra Maharasta \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Shah Clinic \nDoctor Name : Dr.Shah \nAddress : 90, Dadar, Near Dadar Nagr Have Maharastra \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")


def kothrud_best_Clinic() :
        print("Here is Best Clinic in Kothrud Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Aarogya Care Clinic  \n2.)Healing Roots Clinic \n3.)Niramay Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Aarogya Care Clinic \nDoctor Name : \nDr.Aarogya \nAddress : 56, Kothrud, Near Kothrud Mall  Circle Maharastra \nContact No : +91 98765 43210")
                    break

                elif option == "2" :
                    print("You Have Selected Healing Roots Clinic \nDoctor Name : \nDr.Mahesh \nAddress : 78, Kothrud Main Road, Near Realiance Mart Bus Stand Kothrud ,Maharashtra \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Niramay Clinic \nDoctor Name : \nDr.Niramay \nAddress : 90, Kothrud, Front Of Crystal School  Kothrud ,Maharashtra \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")



def shivaji_nagar_best_Clinic() :
        print("Here is Best Clinic in Shivaji Nagar Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Maitri Clinic  \n2.)Sanjeevani Clinic \n3.)Swasthya Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Maitri Clinic \nDoctor Name : Dr.Maitri \nAddress : 56, Shivaji Nagar, Near Police Thane Circle Sivaji Nagar Maharashtra \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Sanjeevani Clinic \nDoctor Name : Dr.Sanjeevani \nAddress : 78, Shivaji Nagar Main Road, Near Manjalpur Bus Stand Sivaji Nagar Maharashtra \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Swasthya Clinic \nDoctor Name : Dr.Swasthya \nAddress : 90, Shivaji Nagar, Near Gandhi Circle ,Sivaji Nagar Maharashtra \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")




def hadapsar_best_Clinic() :
        print("Here is Best Clinic in Hadapsar Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Arogya Dham Clinic  \n2.)Nidan Clinic \n3.)Jeevan Jyoti Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Arogya Dham Clinic \nDoctor Name : Dr.Arogya \nAddress : 56, Hadapsar, At Kareli Chok Hadapsar Maharashtra \nContact No : +91 98765 43210")
                    break

                elif option == "2" :
                    print("You Have Selected Nidan Clinic \nDoctor Name : Dr.Nidan \nAddress : 78, Hadapsar Main Road, Near Master Tution Classes Hadapsar Maharashtra \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Jeevan Jyoti Clinic \nDoctor Name : Dr.Jeevan Jyoti \nAddress : 90, Hadapsar, In Front Of Sad Guru School Hadapsar Maharashtra \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")


def civil_lines_best_Clinic() :
        print("Here is Best Clinic in Civil Lines Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Sanjeevani Clinic  \n2.)Arogya Clinic \n3.)Niramay Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Sanjeevani Clinic \nDoctor Name : Dr.Sanjeevani \nAddress : 56, Civil Lines, Near Chinoy BunGlows, Civil Lines Maharashtra \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                   
                  print("You Have Selected Arogya Clinic \nDoctor Name : Dr.Arogya \nAddress : 78, Civil Lines Main Road, Toward To Ganesh Kirana Store ,Civil Lines Maharashtra \nContact No : +91 87654 32109")
                  break
                elif option == "3" :
                    print("You Have Selected Niramay Clinic \nDoctor Name : Dr.Niramay \nAddress : 90, Civil Lines, in Parivar Area,Civil Lines Maharashtra \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()

        except Exception as e :
            print("Please Enter Valid Option")

def sitabuldi_best_Clinic() :
        print("Here is Best Clinic in Sitabuldi Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Dhanwantari Clinic  \n2.)Swasthya Clinic \n3.)Jeevan Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Dhanwantari Clinic \nDoctor Name : Dr.Dhanwantari \nAddress : 56, Sitabuldi, Near Sheth Bundglows , Sitabuldi Maharastra \nContact No : +91 98765 43210")
                    break
                elif option == "2" :
                    print("You Have Selected Swasthya Clinic \nDoctor Name : Dr.Swasthya \nAddress : 78, Sitabuldi Main Road, Near Sivaji Park ,Sitabuldi Maharastra \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Jeevan Clinic \nDoctor Name : Dr.Jeevan \nAddress : 90, Sitabuldi,At Laxmi Flat , Sitabuldi Maharastra  \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()

        except Exception as e :
            print("Please Enter Valid Option")

def dharampeth_best_Clinic() :
        print("Here is Best Clinic in Dharampeth Area")
        try : 
          option = input("\nSelect An Best Clinic Thease All Are Best : \n1.)Arogya Dham Clinic  \n2.)Nidan Clinic \n3.)Jeevan Jyoti Clinic\nYour Choice : ").strip()
          while True :
                if option == "1" :
                    print("You Have Selected Arogya Dham Clinic \nDoctor Name : Dr.Vraj \nAddress : 56, Dharampeth, Toward To SSV School  Dharampeth Maharashtra \nContact No : +91 98765 43210")
                    break

                elif option == "2" :
                    print("You Have Selected Nidan Clinic \nDoctor Name : Dr.Nidan \nAddress : 78, Dharampeth Main Road, At Menna Chok  Dharampeth Maharashtra \nContact No : +91 87654 32109")
                    break
                elif option == "3" :
                    print("You Have Selected Jeevan Jyoti Clinic \nDoctor Name : Dr.Jeevan Jyoti \nAddress : 90, Dharampeth, Near By Wel & Care Hospital, Dharampeth Maharashtra \nContact No : +91 76543 21098")
                    break
                else :
                    option = input("Please Enter Valid Option For Hospital ✔ ").strip()
        except Exception as e :
            print("Please Enter Valid Option")


class Hospital:
    def __init__ (self) :
        print("\nOK Your Serach Engine is Ready To User ✔\n")
    def select_state(self) :
            state = input("\nEnter Your State To Get Best Local Clinic Support \n1.)Gujrat\n2.)Maharashtra\nYour Choice : ")
            try :
                while True :
                        if state == "1" :
                             print("\nOk Lets Find Best Clinic In Gujrat ✔")
                             city = input("\nEnter Your City Name in Gujrat \n1.)Vadodara \n2.)Ahemdabad \n3.)Surat \nYour Choice :  ").strip()
                             if city == "1" :
                                  print("\nOk Lets Find Best Clinic In Vadodara ✔")
                                  area = input("Enter Your Area Name in Vadodara \n1.)Alkapuri \n2.)Gotri \n3.)Manjalpur \nYour Choice : ").strip()

                                  if area == "1" :
                                       alkapuri_best_clinic()
                                       break
                                  elif area == "2" :
                                       gotri_best_clinic()
                                       break
                                  elif area == "3" :
                                       manjalpur_best_clinic()
                                       break
                                  else :
                                       area = input("Please Enter Valid Area Name : ").strip().title()
                             elif city == "2" :
                                  print("\nOk Lets Find Best Clinic In Ahemdabad ✔")
                                  area = input("\nEnter Your Area Name in Ahemdabad \n1.)Navrangpura \n2.)Paldi \n3.)Vastrapur \nYour Choice : ").strip()
                                  if area == "1" :
                                       navrang_pura_best_clinic()
                                       break
                                  elif area == "2" :
                                       paldi_best_clinic()
                                       break
                                  elif area == "3" :
                                       vasatrapur_best_clinic()
                                       break
                                  else :
                                       area = input("Please Enter Valid Area Name : ").strip().title()
                             elif city == "3" :
                                    print("\nOk Lets Find Best Clinic In Surat ✔")
                                    area = input("\nEnter Your Area Name in Surat \n1.)Adajan \n2.)Udhna \n3.)Varachha \nYour Choice : ").strip()
                                    if area == "1" :
                                         adajan_best_Clinic()
                                         break
                                    elif area == "2" :
                                         udhna_best_Clinic()
                                         break
                                    elif area == "3" :
                                         varachha_best_Clinic()
                                         break
                                    else :
                                         area = input("Please Enter Valid Area Name : ").strip().title()

                        elif state == "2" :
                             print("\nOk Lets Find Best Clinic In Maharashtra ✔")
                             city = input("\nEnter Your City Name in Maharashtra \n1.)Mumbai \n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
                             if city == "1" :
                                  print("\nOk Lets Find Best Clinic In Mumbai ✔")
                                  area = input("\nEnter Your Area Name in Mumbai \n1.)Andheri \n2.)Bandra \n3.)Dadar \nYour Choice : ").strip()
                                  if area == "1" :
                                       andheri_best_Clinic()
                                       break
                                  elif area == "2" :
                                       bandra_best_Clinic()
                                       break
                                  elif area == "3" :
                                       dadar_best_Clinic()
                                       break
                                  else :
                                       area = input("Please Enter Valid Area Name : ").strip().title()
                             elif city == "2" :
                                  print("\nOk Lets Find Best Clinic In Pune ✔")
                                  area = input("\nEnter Your Area Name in Pune \n1.)Kothrud \n2.)Shivaji Nagar \n3.)Hadapsar \nYour Choice : ").strip()
                                  if area == "1" :
                                       print("Here is Best Clinic in Kothrud Area")
                                       kothrud_best_Clinic()
                                       break
                                  elif area == "2" :
                                       print("Here is Best Clinic in Shivaji Nagar Area")
                                       shivaji_nagar_best_Clinic()  
                                       break
                                  elif area == "3" :
                                       
                                       hadapsar_best_Clinic()
                                       break
                                  else :
                                       area = input("Please Enter Valid Area Name : ").strip().title()
                             elif city == "3" :
                                  print("\nOk Lets Find Best Clinic In Nagpur ✔")
                                  area = input("\nEnter Your Area Name in Nagpur \n1.)Civil Lines \n2.)Sitabuldi \n3.)Dharampeth \nYour Choice : ").strip()
                                  if area == "1" :
                                       
                                       civil_lines_best_Clinic()
                                       break
                                  elif area == "2" :
                                       
                                       sitabuldi_best_Clinic()
                                       break
                                  elif area == "3" :
                                       
                                       dharampeth_best_Clinic()
                                       break
                                  else :
                                       area = input("Please Enter Valid Area Name : ").strip().title()
                             else :
                                  city = input("Please Enter Valid City Name : ").strip().title()

                 
                        
                        
            except Exception as e :
                print("Please Enter Valid State Name")
            pass




# ________________________________________________________________________________________________________

# X Hospital Illness Hospital Finder


def ahemdabad_illness_hospital() :
   print("Ok Enter Your illness To Find Best Hospital in Ahemdabad ✔")
   try :
      while True :
         option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
         if option == "1" :
            cancer_hospital = ['Apollo Hospital','CIMS Hospital','HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital']
            print("Best Hospital For Cancer in Ahemdabad is : ",random.choice(cancer_hospital))
            break
         elif option == "2" :
            heart_hospital = ['Apex Heart Institute','U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad']
            print("Best Hospital For Heart in Ahemdabad is : ",random.choice(heart_hospital))
            break
         elif option == "3" :
            kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Apollo Hospital','CIMS Hospital']
            print("Best Hospital For Kidney Stone in Ahemdabad is : ",random.choice(kidney_hospital))
            break
         elif option == "4" :
            surgical_hospital = ['Marengo CIMS Hospital','Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
            print("Best Hospital For Surgical in Ahemdabad is : ",random.choice(surgical_hospital))
            break
   except Exception as e :
      print("The Occured Error is ",e)

def vadodara_illness_hospital() :
    print("Ok Enter Your illness To Find Best Hospital in Vadodara ✔")
    try :
      while True :
         option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
         if option == "1" :
            cancer_hospital = ['Sterling Hospitals','Himalaya Cancer Hospital & Research Institute','HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital']
            print("Best Hospital For Cancer in Vadodara is : ",random.choice(cancer_hospital))
            break
         elif option == "2" :
            heart_hospital = ['Baroda Heart Institute & Research Centre','Bankers Heart Institute','Bankers Heart & Multispeciality Hospital','U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad']
            print("Best Hospital For Heart in Vadodara is : ",random.choice(heart_hospital))
            break
         elif option == "3" :
            kidney_hospital = ['Kidney Care Hospital Dr Pratik D Shah','Gujarat Superspeciality Hospital','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Apollo Hospital','CIMS Hospital']
            print("Best Hospital For Kidney Stone in Vadodara is : ",random.choice(kidney_hospital))
            break
         elif option == "4" :
            surgical_hospital = ['Gujarat Surgical Hospital','Parth Surgical Hospital','NEEJ SURGICAL HOSPITAL','Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
            print("Best Hospital For Surgical in Vadodara is : ",random.choice(surgical_hospital))
            break
    except Exception as e :
      print("The Occured Error is ",e)

def surat_illness_hospital() :
   print("Ok Enter Your illness To Find Best Hospital in Surat ✔")
   try :
      while True :
         option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
         if option == "1" :
            cancer_hospital = ['Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
            print("Best Hospital For Cancer in Surat is : ",random.choice(cancer_hospital))
            break
         elif option == "2" :
            heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
            print("Best Hospital For Heart in Surat is : ",random.choice(heart_hospital))
            break
         elif option == "3" :
            kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
            print("Best Hospital For Kidney Stone in Surat is : ",random.choice(kidney_hospital))
            break
         elif option == "4" :
            surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
            print("Best Hospital For Surgical in Surat is : ",random.choice(surgical_hospital))
            break
   except Exception as e :
      print("The Occured Error is ",e)


def Gujrat() :
   print("Ok lets Find Best Hospital For You in Gujrat ✔")
   city = input("\nSelect Your City in Gujrat \n1.)Ahemdabad \n2.)Vadodara \n3.)Surat \nYour Choice : ").strip()
   try :
      if city == "1" :
         ahemdabad_illness_hospital()
      elif city == "2" :
         vadodara_illness_hospital()
      elif city == "3" :
         surat_illness_hospital()
   except :
      print("Please Select Vaild City ✔") 


def tamil_nadu_illness_hospital() :
      print("Ok Enter Your illness To Find Best Hospital in Tamil Nadu ✔")
      try :
         while True :
            option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
            if option == "1" :
               cancer_hospital = ['HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
               print("Best Hospital For Cancer in Tamil Nadu is : ",random.choice(cancer_hospital))
               break
            elif option == "2" :
               heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
               print("Best Hospital For Heart in Tamil Nadu is : ",random.choice(heart_hospital))
               break
            elif option == "3" :
               kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
               print("Best Hospital For Kidney Stone in Tamil Nadu is : ",random.choice(kidney_hospital))
               break
            elif option == "4" :
               surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
               print("Best Hospital For Surgical in Tamil Nadu is : ",random.choice(surgical_hospital))
               break
      except Exception as e :
         print("The Occured Error is ",e)





def Tamil_nadu() :
   print("Ok lets Find Best Hospital For You in Tamilnadu ✔")
   try :
      while True :
         city = input("\nSelect Your City in Tamil Nadu \n1.)Chennai \n2.)Coimbatore \n3.)Madurai \nYour Choice : ").strip()
         if city == "1" :
            tamil_nadu_illness_hospital()
            break
         elif city == "2" :
            tamil_nadu_illness_hospital()
            break
         elif city == "3" :
            tamil_nadu_illness_hospital()
            break

   except Exception as e :
      print("The Occured Error is ",e)("Please Select Vaild City ✔") 


def maharastra_illness_hospital() :
   print("Ok Enter Your illness To Find Best Hospital in Maharastra ✔")
   try :
        while True :
             option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
             if option == "1" :
                cancer_hospital = ['HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
                print("Best Hospital For Cancer in Maharastra is : ",random.choice(cancer_hospital))
                break
             elif option == "2" :
                heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
                print("Best Hospital For Heart in Maharastra is : ",random.choice(heart_hospital))
                break
             elif option == "3" :
                kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
                print("Best Hospital For Kidney Stone in Maharastra is : ",random.choice(kidney_hospital))
                break
             elif option == "4" :
                surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
                print("Best Hospital For Surgical in Maharastra is : ",random.choice(surgical_hospital))
                break
             else :
                print("Please Select Above illness Option ✔")
   except Exception as e :
      print("The Occured Error is ",e)


def karnataka_illness_hospital() :
       print("Ok Enter Your illness To Find Best Hospital in Karnataka ✔")
       try :
           while True :
               option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
               if option == "1" :
                   cancer_hospital = ['HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
                   print("Best Hospital For Cancer in Karnataka is : ",random.choice(cancer_hospital))
                   break
               elif option == "2" :
                   heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
                   print("Best Hospital For Heart in Karnataka is : ",random.choice(heart_hospital))
                   break
               elif option == "3" :
                   kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
                   print("Best Hospital For Kidney Stone in Karnataka is : ",random.choice(kidney_hospital))
                   break
               elif option == "4" :
                   surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
                   print("Best Hospital For Surgical in Karnataka is : ",random.choice(surgical_hospital))
                   break
               else :
                   print("Please Select Above illness Option ✔")
       except Exception as e :
           print("The Occured Error is ",e)


def jammu_and_kashmir_illness_hospital() :  
    print("Ok Enter Your illness To Find Best Hospital in Jammu & Kashmir ✔")
    try :
                
        
            while True :
                option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
                if option == "1" :
                    cancer_hospital = ['HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
                    print("Best Hospital For Cancer in Jammu & Kashmir is : ",random.choice(cancer_hospital))
                    break
                elif option == "2" :
                    heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
                    print("Best Hospital For Heart in Jammu & Kashmir is : ",random.choice(heart_hospital))
                    break
                elif option == "3" :
                    kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
                    print("Best Hospital For Kidney Stone in Jammu & Kashmir is : ",random.choice(kidney_hospital))
                    break
                elif option == "4" :
                    surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
                    print("Best Hospital For Surgical in Jammu & Kashmir is : ",random.choice(surgical_hospital))
                    break
                else :
                    print("Please Select Above illness Option ✔")
    except Exception as e :
        print("The Occured Error is ",e)
        print("Please Try Again ✔")

def madhya_pradesh_illness_hospital() :
    print("Ok Enter Your illness To Find Best Hospital in Madhya Pradesh ✔")
    try :
                
        
            while True :
                option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
                if option == "1" :
                    cancer_hospital = ['HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
                    print("Best Hospital For Cancer in Madhya Pradesh is : ",random.choice(cancer_hospital))
                    break
                elif option == "2" :
                    heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
                    print("Best Hospital For Heart in Madhya Pradesh is : ",random.choice(heart_hospital))
                    break
                elif option == "3" :
                    kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
                    print("Best Hospital For Kidney Stone in Madhya Pradesh is : ",random.choice(kidney_hospital))
                    break
                elif option == "4" :
                    surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
                    print("Best Hospital For Surgical in Madhya Pradesh is : ",random.choice(surgical_hospital))
                    break
                else :
                    print("Please Select Above illness Option ✔")
    except Exception as e :
        print("The Occured Error is ",e)
        print("Please Try Again ✔")

def telngana_illness_hospital() :
    print("Ok Enter Your illness To Find Best Hospital in Telngana ✔")
    try :
                
        
            while True :
                option = input("\nSelect Your illness \n1.)Cancer \n2.)Heart \n3.)Kidney Stone \n4.)Surgical \nYour Choice : ").strip()
                if option == "1" :
                    cancer_hospital = ['HCG Cancer Center','Navkar Surgical Hospital','Shalby Hospital','Apollo Spectra Hospitals']
                    print("Best Hospital For Cancer in Telngana is : ",random.choice(cancer_hospital))
                    break
                elif option == "2" :
                    heart_hospital = ['U N Mehta Institute of Cardiology & Research Centre','Apollo Hospital International Limited Ahmedabad','Surat Heart Institute & Research Centre']
                    print("Best Hospital For Heart in Telngana is : ",random.choice(heart_hospital))
                    break
                elif option == "3" :
                    kidney_hospital = ['Devasya Super Speciality Kidney Institute and Research Centre','Devasya Super Speciality Kidney & Multi Speciality Hospitals','Mahavir Hospitals and Sunshine Global Hospital both have strong oncology departments','CIMS Hospital']
                    print("Best Hospital For Kidney Stone in Telngana is : ",random.choice(kidney_hospital))
                    break
                elif option == "4" :
                    surgical_hospital = ['Pinaksh Hospital','Apollo Hospital','CIMS Hospital','Shalby Hospital']
                    print("Best Hospital For Surgical in Telngana is : ",random.choice(surgical_hospital))
                    break
                else :
                    print("Please Select Above illness Option ✔")
    except Exception as e :
        print("The Occured Error is ",e)
        print("Please Try Again ✔")

   
def maharastra() :
   print("Ok lets Find Best Hospital For You in Maharastra ✔")
   try :
      while True :
         city = input("\nSelect Your City in Maharastra \n1.)Mumbai \n2.)Pune \n3.)Nagpur \nYour Choice : ").strip()
         if city == "1" :
            maharastra_illness_hospital()
            break
         elif city == "2" :
            maharastra_illness_hospital()
            break
         elif city == "3" :
            maharastra_illness_hospital()
            break

   except Exception as e :
      print("The Occured Error is ",e)("Please Select Vaild City ✔")





def karnataka() :
   print("Ok lets Find Best Hospital For You in Karnataka ✔")
   karnataka_illness_hospital()

def jammu_and_kashmir() :
   print("Ok lets Find Best Hospital For You in Jammu & Kashmir ✔")
   jammu_and_kashmir_illness_hospital()


def madhya_pradesh() :
   print("Ok lets Find Best Hospital For You in Madhya Pradesh ✔")
   madhya_pradesh_illness_hospital()



def telngana() :
   print("Ok lets Find Best Hospital For You in Telngana ✔")

   telngana_illness_hospital()


def select_option() :
    select = input("\nOk Please Select Your State \n1.)Gujrat \n2.)MahaRastra \n3.)Karnataka \n4.)TamilNadu \n5.)MadhyaPradesh \n6.)Telngana \n7.)Jammu & Kashmir \nYour Choice :  ").strip()
    try :
        if select == "1" :
         Gujrat()
        elif select == "2" :
           maharastra()
        elif select == "3" :
           karnataka()
        elif select == "4" :
           Tamil_nadu()
        elif select == "5" :
           madhya_pradesh()
        elif select == "6" :
           jammu_and_kashmir()
        elif select == "7" :
           telngana()
        else :
           print("Please Select Above State Option ✔")
        
    except :
       print("Give input in As it Mentioned ✔")




welcome = input("Welcome To Smart X Hospital : ")

option = input("\nSelect An Option \n1.)Find Best Clinic Near You \n2.)Find Best Hospital For Your illness \nYour Choice : ").strip()

try :
    if option == "1" :
      h = Hospital()
      h.select_state()
    elif option == "2" :
      select_option()
    else :
      print("Please Select Above Option ✔")    
except Exception as e:
    print("The Occured Error is ",e)
    print("Please Try Again ✔")