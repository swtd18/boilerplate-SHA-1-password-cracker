import hashlib

def crack_sha1_hash(hash,use_salts=False):

    with open("top-10000-passwords.txt","r") as f:
        found=False
        for line in f:
            if(use_salts):
                with(open("known-salts.txt"))as f2:
                    for lin in f2:
                        preappended=hashlib.sha1((lin.strip()+line.strip()).encode("utf-8")).hexdigest()
                        appended= hashlib.sha1((line.strip()+lin.strip()).encode("utf-8")).hexdigest()
                        if hash == preappended or hash==appended:
                            found=True
                            break
                f2.close()        
                if(found):
                     break
            else :
                if hash == hashlib.sha1(line.strip().encode("utf-8")).hexdigest():
                    found=True
                    break 
        f.close()                
        if(found):
            return line.strip()
        else :
            f.close()
            return "PASSWORD NOT IN DATABASE"
  