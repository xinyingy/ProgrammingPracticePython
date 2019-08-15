# -*- coding: UTF-8 -*-
import random
class Names(object):
    def __init__(self):
        self.femaleFirstNames = ["Aditi  ","Aishwarya","Akhila","Ambika  ","Ami  ","Amita","Amrita","Ananya","Anasuya  ","Angelika ","Anjali","Ankita","Anu ","Anupama  ","Anuradha ","Anushree","Apoorva  ","Arpita","Arti  ","Arundhati  ","Bipasha","Damayanti  ","Deepa","Deepali","Deepika","Deepti","Devanshi","Dhanishka","Disha  ","Eva ","Gayatri ","Gita  ","Gitanjali  ","Harshita","Heera","Hemalata","Indira ","Indrani ","Indumati","Jara  ","Jesminder","Juhi ","Kanika ","Karthika ","Kavita","Keerthi","Kirtan","Kumudini","Lakshanya","Lata","Latha","Latika","Leela ","Leila ","Lena ","Madhumita","Madhuri","Mallika","Maneet","Manjula","Manorama","Maya  ","Meghana ","Meghna ","Mira  ","Mohini ","Nadia","Nahla ","Naila ","Namrata","Neelam  ","Neetu","Neha","Niharika","Nikita  ","Nisha","Nupur","Padmavati","Pallavi  ","Parvati  ","Phanita","Poonam","Poulomi","Pranati","Pratibha","Pratiksha","Preeti","Priya  ","Priyanka","Puja","Rajadhi","Rajathi","Ramya ","Ramya  ","Rana ","Rani","Rashmi","Rati  ","Rekha  ","Richa","Ritwika","Roopa","Saloni","Sanah","Sandhya","Sania","Saranya  ","Sarita","Satyana","Savitri","Sharmila","Sheela  ","Sheetal","Shilpa","Shreya","Shweta","Simran ","Sneha","Sonali","Sudha","Sujata ","Sulochana","Sushma","Susmita","Tanisha ","Tanushree","Tejal","Tejaswi","Tina  ","Uma  ","Uzma","Varsha","Vibha","Vijayalakshmi","Yamini"]
        self.maleFirstNames = ["Abhay","Abhinav","Abhishek ","Adarsh","Adesh","Adhar","Adi ","Aditya ","Ajay  ","Ajish","Ajit  ","Akhil","Akshat","Amarjit","Ambika  ","Amit","Ammar ","Amrik","Ananya","Aniket","Anil  ","Anirban","Aniruddha  ","Ankit","Anuj ","Anup","Anupam  ","Anurag","Apoorva  ","Arhaan","Arjun ","Arjun Singh ","Arnab","Arun  ","Arvind","Arya ","Aseem","Ashwin  ","Bali ","Baltej","Bellamkonda ","Bhagwant","Bharat","Bhavesh","Bhupinder","Bhushan","Bibin","Biju","Binu","Birendra ","Bishamber","Byramjee","Chandrajit","Dayanidhi","Debabrata","Deepak","Devendra","Devesh","Dharanidhar","Dheeraj","Dhinakaran","Dileesh","Dinesh","Dipankar","Dnyandeo","Ekram","Elangovan","Ganesh  ","Ganga Prasad ","Ganpatrao","Giridhar","Girish","Gnanasekaran","Gopinathan","Govindrao","Gurcharan","Gurunath","Hansraj","Hanuman ","Hara  ","Harish","Harjit","Harmeet","Harsh","Hitesh","Ira ","Ishana","Jaipal","Jalaj","Jayant ","Jitendra  ","Kalimuthu","Kalpesh","Kantilal","Karan  ","Karthik","Karthikeyan","Kaushal","Kaustubh","Kazi  ","Kishor","Kishore ","Kripesh","Krishnappa","Krishnayya","Kulbhushan","Kumar ","Lakshan","Lakshman ","Mahboob","Mahendra","Manmohan","Mehar ","Mehul","Mukesh","Munish","Muthuswamy","Nadeem","Nagaraj","Nagraj ","Nana  ","Naranbhai","Narayan ","Naveen","Neeraj","Nibaran","Nihal ","Nihar","Nilesh","Nirav","Nirupam","Nitesh","Nitin","Nripendra","Omkar","Palanivel","Pallav","Pankaj","Phani","Pitamber","Prabodh Chandra","Prakash","Pramod","Pranab","Pranav","Pranay","Prannoy","Prataprao","Pratul","Puran ","Radhanath","Raghu  ","Rahul","Raj ","Raja ","Rajendra ","Rajinder","Rajiv","Rakesh","Ram  ","Ram Narayan ","Ramakant","Ramesh","Ranbir","Randhir","Ranganath","Ratnam","Ratul","Ravichandran","Ravinder","Ravish","Rinjish","Rohit","Sabyasachi","Sachin  ","Sahil ","Saju","Saket","Samar ","Sambhunath  ","Samir","Sancheti","Sandipan","Sanjay","Sarabjit","Sashi","Satish","Satish Chandra","Satyadev","Satyajit","Sekar","Shahbaz","Shailendra","Shankarrao","Sharad","Shekhar","Shikhar  ","Shishir","Shishira","Shreyas"]
        self.lastNames = ["Achari ","Adarsh","Adiga","Advani","Adyanthaya","Agashe","Agrahari ","Agrawal","Ahluwalia","Akhand ","Akkineni","Akula","Alladi","Allana","Alva ","Ankitham","Arora ","Arya ","Atluri","Atreya ","Avanthkar","Bafna","Bahl","Bahri","Bahuguna","Baig","Bairisetty","Bajpai","Balaji","Balasubramaniam","Bali  ","Baliga","Ballal","Ban Sanyasi","Bana ","Banerjee","Banga Arasa","Bangi ","Bansal","Bapat","Barad ","Barman ","Barot ","Barthwal","Bartwal","Basak ","Basu","Bayya","Beg Khan","Bendre","Bezawada","Bhaduri","Bhagwat ","Bhagwati","Bhalsod","Bhamra","Bhandarkar","Bhargava","Bhaskaran","Bhat","Bhatia ","Bhatnagar","Bhaṭṭa","Bhau","Bhaura","Bhimwal","Bholowalia","Bhonsle","Bhowal","Bhowmick","Bindra","Binny","Bishnoi","Biswas","Bohra","Bollimunta","Bose ","Brahma ","Brahmbhatt","Buksh","Bulusu","Burdak","Byrraju","Cariappa","Chadalavada","Chakladar","Chakyar","Chambial","Chandavarkar","Chandola","Chandra","Chandrachud","Channar ","Charan","Chatterjee","Chattopadhyay","Chattopadhyaya","Chauhan","Chauhan ","Chennamaneni","Cherian","Cherukuri","Chettiar","Chhibber","Chishti ","Chopra","Chowdhury","Chudasama","Chutia ","Cukkemane","Dabas ","Dabral ","Daivajna ","Damania","Damodaran","Das ","Dasari","Datt","De ","Deb ","Debbarma","Debnath","Deengar","Deol","Desai","Deshpande","Dhamala","Dhankhar","Dhar ","Dharan ","Dharker","Dhillon","Dholia","Dhromer","Dikshit","Dogra","Dogra Rajput","Doshi","Dravid ","Dubey","Duraisamy","Dutta","Dwaram","Dwivedi","Emani","Flora ","Gadhavi","Gaekwad","Gaekwad ","Gahlot","Gaidher","Gairola","Galla","Gandhi ","Ganguly ","Ganti","Garg","Garimella","Gayen","Ghanchi","Ghatak ","Ghosh","Godbole","Goenka","Gogineni","Gokhale","Gounder","Gowda ","Goyal","Grover ","Guha ","Gummadi","Gupta","Guptan","Gurindagunta","Gurunath","Gurung ","Gururani","Haksar","Hatwal","Havyaka ","Hazarika","Hebbar","Hegde","Hiremath","Howlader","Hoysala ","Hunjan","Hussaini ","Inamdar ","Ishwar ","Iyengar","Iyer","Jadaun","Jagtap","Jaitly","Jandhyala","Jha ","Jhaveri","Jindal","Joshi","Kabiraj","Kadanthodu","Kaimal","Kakarla","Kallam","Kalunkhe","Kamat","Kamdar","Kandhari","Kandukuri","Kansal","Kanwat","Kapoor","Kar suffix","Karhade ","Karnik","Kasu","Katiyar","Kaul","Kaur","Kaushal","Kaushik","Kaviraj","Khakh","Khan ","Khanolkar","Khare","Khatri ","Khatri Uppal ","Khondakar","Khosla","Khullar","Kichlu","Kidambi","Kodakkadan","Kohli","Kohli ","Kollannur","Kommineni","Koneru","Konidela ","Kothari","Kotikalapudi","Kotwal ","Kovelamudi","Krishnamurti","Kuchchal","Kudva","Kulkarni","Kumar","Kurian","Labbay","Lahoti","Lakhani ","Lakra","Lakshman ","Lal","Lal ","Lau ","Lone ","Machingal","Madathil","Madhunapantula","Mahadevan","Maharaja","Mahawar Koli","Mahto","Maji ","Majji","Majumdar","Makkar","Makur","Malladi","Mallya","Mandal ","Mannava ","Maraj","Marathe","Maru ","Mathai","Matharu","Mathur sub","Mattoo","Mazumdar","Medhekar","Meena","Mehra","Mehta","Menariya","Menon ","Mirdha","Mishra","Mistry ","Mitra ","Modi ","Mohan ","Mohanty","Mohapatra","Mohini ","Mokkapati","Moolgaokar","Moturi","Mudaliar","Mudartha","Mudumbai","Mukherjee","Mukhi","Mulla ","Mullapudi","Munshi","Muppavarapu","Murmu","Murthy","Muttamsetty","Mynampati","Nadar ","Nadkarni","Nadvi","Nagaraj","Nagraj ","Nair","Nalli ","Nambeesan","Nambiar ","Nanda ","Nandamuri","Narayan ","Nath ","Natoo","Naudiyal","Nayak ","Nayanar ","Nayar","Nedumpally","Negi ","Nehra","Nigam","Ningombam","Nischal","Nookala","Noorani","Oberoi","Odedara","Omar Vaishya","Oommen ","Padamadan","Padukone","Pai ","Paidi","Pal ","Palagummi","Paliwal","Pallavaraiyan ","Pamulaparthi","Pandey","Pani","Panikkar","Pannaiyar ","Pant ","Parkhi","Paruchuri","Parupalli","Pasupuleti","Patange","Pathak","Pathani","Patharkar","Patni ","Patrayani","Pavuluri","Pawar ","Peeris","Pendharkar","Pendyala","Penna ","Perumal","Phukan","Phulkian Misl","Pilgaonkar ","Pillai Kerala ","Pillai ","Pisharody","Poddar","Potti","Prabhu","Prasad ","Pujari","Puntambekar","Puri ","Pusapati","Ragam ","Raghavan","Rai ","Raj Mistry","Rajendran ","Ram ","Ramachandran","Rane ","Ranganathan","Rangappa","Rastogi","Rath Odia ","Rattu Punjabi ","Raut ","Ravilla","Ray ","Reddiar","Rigvedi","Rohatgi","Rohit ","Roy","Sabharwal","Sahni","Sahu","Saikia","Saini","Salpe ","Samaga","Sambandam","Sammaat","Samudrala","Sandbhor","Sanghani","Sanghrajka","Sanghvi","Sankaramanchi","Sankhwar","Sapru","Sarbadhikari","Sarpal","Sarvaiya","Sastry","Satamkar","Scindia","Seerla","Sehgal","Seksaria","Semwal","Sethi","Sethia ","Shah ","Shah ","Shahalia","Shaktawat","Sharma","Shenoy","Shett","Shetty","Shewale","Shokeen","Shome","Shrimal Jain","Shroff","Shyam","Singh","Singhai","Singhal","Singhpuria Misl","Singri singiri","Sinha","Sisodia","Sodhi","Solanki","Soni ","Sonsale","Sonti","Srivastava","Subramaniam","Sudhapalli","Sukumaran ","Suravaram ","Suryadevara","Suryanarayana","Sutradhar ","Swarup","Talati","Tallapaka","Tandon","Taneja","Tanguturi","Tari Kashmiri tribe","Tariyal","Tatineni","Tergaonkar","Thakkar","Thakore Saheb of Rajkot","Thakur ","Thandan","Thapar ","Thind","Thirumulpad","Thota","Thukral","Tibrewal","Tipirneni","Tiwari","Tottempudi","Tripathi","Trivedi","Twashta Kasar","Tyagi","Udayar ","Uniyal","Unni Indian ","Unnikrishnan","Upadhyay","Upreti","Urs ","Vaidya","Vaidyar","Valiathan","Vangapandu","Vangaveeti","Vankayala","Varadkar ","Varma ","Varman ","Varshney","Vartak","Vaswani","Vats ","Vavilla","Vedam","Vedantam","Veturi","Vinjamuri","Viswanathan","Vithayathil","Vohra","Wadhwa","Warsi","Yadav","Zacharias ","Zaveri","Zutshi"]

    def get_first_name(self, gender):
        if(gender == 'female'):
            return random.choice(self.femaleFirstNames).strip()
        return random.choice(self.maleFirstNames).strip()

    def get_last_name(self):
        return random.choice(self.lastNames).strip()