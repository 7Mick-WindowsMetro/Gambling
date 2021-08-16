import pickle,os

def main():
    newname = input("请输入你的新昵称：")
    if newname != "":
        info[0] = newname
    input("设置成功！请按回车键退出...")

if __name__ == "__main__":
    binpath = os.path.expanduser("~\\usrinfo.dat")
    if os.path.exists(binpath):
        with open(binpath,"rb") as f:
            try:
                info = pickle.load(f)
                if not isinstance(info,list) or not len(info) == 3:
                    raise ValueError("User information file error!")
            except ValueError as err:
                print("错误：" + str(err))
            else:
                main()
        with open(binpath,"wb") as f:
            pickle.dump(info,f)
    else:
        with open(binpath,"wb") as f:
            info = ["Guest",1,10000]
            pickle.dump(info,f)
