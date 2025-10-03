class Solution:
    def infixtoPostfix(self, s):
        #code here
        d={"^":3,"*":2,"/":2,"+":1,"-":1,"(":-1,")":-1}
        st=[]
        ans=""
        for i in s:
            if i not in d:
                ans+=i
            if i=="(":
                st.append("(")
            if i in d and i!=")" and i!="(" :
                if st:
                    while st and st[-1] !="(" and (d[st[-1]] > d[i] or (d[st[-1]] == d[i] and i != "^")):
                        ans+=st.pop()
                    st.append(i)
                else:
                    st.append(i)
            if i==")":
                while st and st[-1]!="(":
                    ans+=st.pop()
                if st and st[-1]=="(":
                    st.pop()

        while st:
            ans+=st.pop()
        return ans
