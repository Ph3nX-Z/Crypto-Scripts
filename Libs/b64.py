b64 = lambda x:"".join(["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[int(i,2)] for i in (lambda lst:[lst[i*6:(i+1)*6] for i in range((len(lst)+6)//6 )])("".join([format(ord(i),'08b') for i in x])) if i!=""])