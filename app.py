from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from time import sleep


app = Flask(__name__)


@app.route("/")
def hello():
    
    r=requests.get('https://api.covid19india.org/data.json')
   
    return "HEllo"









@app.route("/sms", methods=['POST'])
def sms_reply():
 """Respond to incoming calls with a simple text message."""

    
    
 msg = request.form.get('Body')

 states= [x.upper() for x in ['Maharashtra','Tamil Nadu','Delhi','Gujarat','Karnataka','Uttar Pradesh','Telangana','Andhra Pradesh','West Bengal','Rajasthan','Haryana','Bihar','Madhya Pradesh','Assam','Odisha','Jammu and Kashmir','Punjab','Kerala','Chhattisgarh','Jharkhand','Uttarakhand','Goa','State Unassigned','Tripura','Manipur','Puducherry','Himachal Pradesh','Ladakh','Nagaland','Chandigarh','Dadra and Nagar Haveli and Daman and Diu','Arunachal Pradesh','Meghalaya','Mizoram','Andaman and Nicobar Islands','Sikkim','Lakshadweep']]
 statecode=['MH','TN','DL','GJ','KA','UP','TG','AP','WB','RJ','HR','BR','MP','AS','OR','JK','PB','KL','CT','JH','UT','GA','UN','TR','MN','PY','HP','LA','NL','CH','DN','AR','ML','MZ','AN','SK','LD'];
 


 resp = MessagingResponse()
 
 r=requests.get('https://api.covid19india.org/data.json')
    #msgn=str(msg)
 try:
        if msg== 'hey' or msg=='hello' or msg== "Hey" or msg=='Hello' or msg=="hi" or msg=="Hi":
            #tmsg= resp.message(" \n Hello, I'm your COVID Companion giving access to crtical information on your finger tips \n\nEnter the statewise code to get details of a particular state \n\n Maharashtra \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: MH \n Tamil Nadu \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: TN \n Delhi \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: DL \n Gujarat \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: GJ \n Karnataka \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: KA \n Uttar Prades \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: UP \n Telangana \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: TG \n Andhra Pradesh \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: AP \n West Bengal  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: WB \n Rajasthan  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: RJ \n Haryana  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: HR \n Bihar \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: BR \n Madhya Pradesh  \t\t\t\t\t\t\t\t\t\t\t\t\t\t: MP \n Assam \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: AS \n Odisha \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: OR \n Jammu and Kashmir \t\t\t\t\t\t\t\t\t\t\t: JK \n Punjab \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: PB \n Kerala \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: KL \n Chhattisgarh  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: CT \n Jharkhand  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: JH \n Uttarakhand  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: UT \n Goa  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: GA \n State Unassigned  \t\t\t\t\t\t\t\t\t\t\t\t\t\t: UN \n Tripura  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: TR \n Manipur  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: MN \n Puducherry  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: PY \n Himachal Pradesh  \t\t\t\t\t\t\t\t\t\t\t\t\t: HP \n Ladakh \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: LA \n Nagaland \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: NL \n Chandigarh \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: CH \n DNHDD (union territory)  \t\t\t\t\t\t\t\t: DN  \n Arunachal Pradesh  \t\t\t\t\t\t\t\t\t\t\t\t: AR \n Meghalaya  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: ML \n Mizoram  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: MZ \n Andaman and Nicobar Islands \t\t: AN \n Sikkim  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: SK \n Lakshadweep  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t: LD")
            
            #else:
            tmsg= resp.message(" \n Hello, I'm *Clippy* a response-based chat bot that gives information about *COVID-19* in *India* on your finger tips  \U0001F604 \U0001F916 \U0001F1EE\U0001F1F3 \n\nEnter the statewise code to get details of a particular state \U0001F4AC \n\n*For Example:* KA for details of Karnataka \U0001F3AD \n\n OR \n\nEnter districtwise code to get details based on district bifercation of a particular state \n\n*District code:* DW(followed by the corresponding statecode like KA) \n\n*For Example:* DWGA for list of Districts in Goa \U0001F3DD \n\n 1. Maharashtra (MH) \n 2. Tamil Nadu (TN) \n 3. Delhi (DL) \n 4. Gujarat (GJ) \n 5. Karnataka (KA) \n 6. Uttar Pradesh (UP) \n 7. Telangana (TG) \n 8. Andhra Pradesh (AP) \n 9. West Bengal (WB) \n 10. Rajasthan (RJ) \n 11. Haryana (HR) \n 12. Bihar (BR) \n 13. Madhya Pradesh (MP) \n 14. Assam (AS) \n 15. Odisha (OR) \n 16. Jammu and Kashmir (JK) \n 17. Punjab (PB) \n 18. Kerala (KL) \n 19. Chhattisgarh (CT) \n 20. Jharkhand (JH) \n 21. Uttarakhand (UT) \n 22. Goa(GA) \n 23. State Unassigned (UN) \n 24. Tripura (TR) \n 25. Manipur (MN) \n 26. Puducherry (PY) \n 27. Himachal Pradesh (HP) \n 28. Ladakh (LA) \n 29. Nagaland (NL) \n 30. Chandigarh (CH) \n 31. DNHDD (union territory) (DN) \n 32. Arunachal Pradesh (AR) \n 33. Meghalaya (ML) \n 34. Mizoram (MZ) \n 35. Andaman and Nicobar Islands (AN) \n 36. Sikkim (SK) \n 37. Lakshadweep (LD)\n\n\n *Stay Home Stay Safe* \U0001F3E0 \U0001F6E1\n\n\nThis message can be called back by greeting Clippy with a \"Hey\Hello\Hi\" \U0001F44B Since *Clippy* is response based chat bot it will only respond relevant queries. \U0001F609 \n\nTo know more about the bot *Type:* *Info* \U0001F440 \U0001F4CE\n\n*Developer:* Santosh.Divakaran \U0001F468\U0000200D\U0001F4BB")
        
            #tmsg= resp.message(" \n Hello, I'm your COVID Companion giving access to crtical information on your finger tips \U0001F604 \U0001F916 \U0001F1EE\U0001F1F3 \n\nEnter the statewise code to get details of a particular state \U0001F4AC \n\n OR \n\nEnter districtwise code to get details based on district bifercation of a particular state \n\n Districtwise code: DW(followed by the corresponding statecode like KA) \n\nFor Example: DWGA for Districtwise detail of Goa \U0001F3DD \n\n 1. Maharashtra (MH) \n 2. Tamil Nadu (TN) \n 3. Delhi (DL) \n 4. Gujarat (GJ) \n 5. Karnataka (KA) \n 6. Uttar Pradesh (UP) \n 7. Telangana (TG) \n 8. Andhra Pradesh (AP) \n 9. West Bengal (WB) \n 10. Rajasthan (RJ) \n 11. Haryana (HR) \n 12. Bihar (BR) \n 13. Madhya Pradesh (MP) \n 14. Assam (AS) \n 15. Odisha (OR) \n 16. Jammu and Kashmir (JK) \n 17. Punjab (PB) \n 18. Kerala (KL) \n 19. Chhattisgarh (CT) \n 20. Jharkhand (JH) \n 21. Uttarakhand (UT) \n 22. Goa(GA) \n 23. State Unassigned (UN) \n 24. Tripura (TR) \n 25. Manipur (MN) \n 26. Puducherry (PY) \n 27. Himachal Pradesh (HP) \n 28. Ladakh (LA) \n 29. Nagaland (NL) \n 30. Chandigarh (CH) \n 31. DNHDD (union territory) (DN) \n 32. Arunachal Pradesh (AR) \n 33. Meghalaya (ML) \n 34. Mizoram (MZ) \n 35. Andaman and Nicobar Islands (AN) \n 36. Sikkim (SK) \n 37. Lakshadweep (LD)")
            tmsg.media("https://cdn.cnn.com/cnnnext/dam/assets/200513170740-coronavirus-questions-answered-illustration-super-169.jpg")
                
            
            #tmsg=resp.message(" \U0001F446 The above message can be called back by greeting  ,   is response based chat bot and will respond relevant queries sent to it \U0001F609  ") 
        elif msg=='Info'or msg=='info':
            resp.message("*Clippy* \U0001F916 is made using Python and Json Scripting and is then hosted on Heroku which then communicates with Twilio to send messages.\n \n*Twilio* is a cloud communications platform which allows you to test and protype messaging via WhatsApp using the Twilio API. Since it is a free to use platform there are restrictions in place like rate of messaging and the channel size which restricted clippy to completely be user friendly ")


        elif msg[:2]=='DW' or  msg[:2]=='Dw'or msg[:2]=='dw' or  msg[:2]=='dW':
            
            x=requests.get('https://api.covid19india.org/state_district_wise.json')
            #dis=x.json()['{}']['Goa']['districtData']
            #resp.message("{}".format(dis))
        
            def extract_values(obj, key):
                """Pull all values of specified key from nested JSON."""
                arr = []

                def extract(obj, arr, key):
                    """Recursively search for values of key in JSON tree."""
                    if isinstance(obj, dict):
                        for k, v in obj.items():
                            if isinstance(v, (dict, list)):
                                extract(v, arr, key)
                            elif k == key:
                                arr.append(v)
                    elif isinstance(obj, list):
                        for item in obj:
                            extract(item, arr, key)
                    return arr

                results = extract(obj, arr, key)
                return results
        
            statec= extract_values(x.json(),msg[2:4])
            discheck=msg[2:4].upper()
            #print(x.json().keys())

            disstates=['State Unassigned', 'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat', 'Himachal Pradesh', 'Haryana', 'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra', 'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Puducherry', 'Rajasthan', 'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
            discodes=['UN', 'AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DL', 'DN', 'GA', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'LA', 'LD', 'MH', 'ML', 'MN', 'MP', 'MZ', 'NL', 'OR', 'PB', 'PY', 'RJ', 'SK', 'TG', 'TN', 'TR', 'UP', 'UT', 'WB']
            
            for p in discodes:
                disI=discodes.index(discheck)
                if discheck==discodes[disI]:
                        Estate=disstates[disI]
                        y=list(x.json()[Estate]['districtData'].keys())
                        num=len(y)
            #print(y)
            #print(num)
            #print(Estate)
            #a=x.json()[Estate]['districtData'][y[0]]['active'] 
            #print(a)

            if msg[-1:].isdigit(): 
                m=int(msg[-1:]) 
                print(y[m-1])
                if m <=num:    
                    a=x.json()[Estate]['districtData'][y[m-1]]['active'] 
                    c=x.json()[Estate]['districtData'][y[m-1]]['confirmed']   
                    d=x.json()[Estate]['districtData'][y[m-1]]['deceased'] 
                    rec=x.json()[Estate]['districtData'][y[m-1]]['recovered'] 
                    
                    resp.message("*District:* {0} \n*Confirmed cases:* {1} \n*Active Cases:* {2}\n*Deaths:* {3} \n*Recovered:* {4} ".format(y[m-1],c,a,d,rec))

            else:
                resp.message(" *Districts for {0}* \n".format(Estate))
            #for tc in range(num):
                #cc=tc+1
            
                resp.message('\n'.join('{}: {}'.format(*k) for k in enumerate(y,1)))

                resp.message("To know the details of a specific district \n\nEnter *DW*(followed by the corresponding statecode like *KA*)(followed index position of the district like *5*)\n\nFor Example: *DWKA5* for displaying details Bengaluru Urban")
            
            
            #print(disstates[16])
            #print(msg[-1:])
            #print(y)

            
                    
            #chunks = [NUM[x:x+4] for x in range(0, len(NUM), 4)]
            #resp.message("District: {0} \nConfirmed cases: {1} \nActive Cases : {2}\nDeaths : {3} \n :{4} :{5}".format(*chunks))
            
            #print(NUM) 
            #print(chunks)  
            #print(":{0} :{1} :{2}".format(cf,df,mn))    
        
    
        else:
                #i=0
            # j=0
                #cf=0
                #df=0
                msgn=msg.upper()
                #try:
                #for m in statecode:
            # i=statecode.index(msgn)
                    #cf=cf+1;
                #if msgn=='KA':
                    #df=df+1
                    # s=states[i] 
                    #a=r.json()['statewise'][i+1]['active'] 
                    # c=r.json()['statewise'][i+1]['confirmed']   
                    #d=r.json()['statewise'][i+1]['deaths']
                    #t=r.json()['statewise'][i+1]['lastupdatedtime']
                            #nb=r.json()['statewise'][i]['statenotes']
                
                l=1;
                for l in range(38) :
                    if msgn==r.json()['statewise'][l]['statecode']:   
                        s=r.json()['statewise'][l]['state']
                        print(l)
                        a=r.json()['statewise'][l]['active'] 
                        c=r.json()['statewise'][l]['confirmed']   
                        d=r.json()['statewise'][l]['deaths']
                        t=r.json()['statewise'][l]['lastupdatedtime']   
                        rec=r.json()['statewise'][l]['recovered']   
                    
                
                
                
                
                #print(l)            
                #print(r.json()['statewise'][l] )
                ##print(type(msgn))
                #print(msgn)
                #print(i)
                #print(type(statecode[l]))
                #print(statecode[l])
            # except:  
                    #for n in states:
                        #j=states.index(msgn)
                        #if msgn==states[j]:
                            #s=states[j] 
                            #a=r.json()['statewise'][j]['active'] 
                            #c=r.json()['statewise'][j]['confirmed']   
                            #d=r.json()['statewise'][j]['deaths']     
                            #t=r.json()['statewise'][j]['lastupdatedtime']
                            #nb=r.json()['statewise'][j]['statenotes']

                # Create reply
                resp = MessagingResponse()
                resp.message("*State:* {0} \n*Confirmed cases:* {1} \n*Active Cases:* {2}\n*Deaths :* {3} \n*Recovered:* {4} \n*Last Updated:* {5} ".format(s,c,a,d,rec,t))

 except :
        resp.message("Oops, that's a wrong query \U0001F47E \nTry entering a statecode or district code or type in *Info* to know more about me: \U0001F916")    
 

 return str(resp)

if __name__ == "__main__":
    app.run(debug=True)