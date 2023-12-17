import streamlit as st
import pandas as pd 
import numpy as np
from sklearn.utils import shuffle
from collections import Counter
from PIL import Image

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
UZT_logo = Image.open('uzt_logo.png')

logo1, title_col, title2_col = st.columns([1,2,2])

with logo1:
    
    st.image(UZT_logo, width=100)

with title_col:
    st.title('We are UZT!!!')
    st.text('Unbroken Zombie Tennis')
    st.text(' ')
    
team_list = []
st.subheader('UZT members')
col1, col2, col3, col4, col41 = st.columns(5)
cnt = 0
with col1: 
    agree1 = st.checkbox('지은')
    agree2 = st.checkbox('유진')
    agree3 = st.checkbox('유나')
with col2:
    agree4 = st.checkbox('이동근')
    agree5 = st.checkbox('구동근')
    agree6 = st.checkbox('광섭')
with col3:
    agree7 = st.checkbox('재성')
    agree8 = st.checkbox('재홍')
    agree9 = st.checkbox('민형')
with col4:
    agree10 = st.checkbox('성환')
    agree11 = st.checkbox('정빈')
    agree12 = st.checkbox('경수')
with col41:
    agree13 = st.checkbox('종우')
    agree14 = st.checkbox('은기')
    agree15 = st.checkbox('동석')

if agree1:
    team_list.append(['지은', 'F', 3.0])
    cnt += 1
if agree2:
    team_list.append(['유진', 'F', 2.5])
    cnt += 1
if agree3:
    team_list.append(['유나', 'M', 2.5])
    cnt += 1
if agree4:
    team_list.append(['이동근', 'M', 3.5])
    cnt += 1
if agree5:
    team_list.append(['구동근', 'M', 2.5])
    cnt += 1
if agree6:
    team_list.append(['광섭', 'M', 3.0])
    cnt += 1
if agree7:
    team_list.append(['재성', 'M', 3.0])
    cnt += 1
if agree8:
    team_list.append(['재홍', 'M', 3.5])
    cnt += 1
if agree9:
    team_list.append(['민형', 'M', 2.5])
    cnt += 1
if agree10:
    team_list.append(['성환', 'M', 2.5])
    cnt += 1
if agree11:
    team_list.append(['정빈', 'M', 3.0])
    cnt += 1
if agree12:
    team_list.append(['경수', 'M', 3.5])
    cnt += 1
if agree13:
    team_list.append(['종우', 'M', 3.0])
    cnt += 1
if agree14:
    team_list.append(['은기', 'M', 3.0])
    cnt += 1
if agree15:
    team_list.append(['동석', 'M', 4.0])
    cnt += 1

list_sum = team_list

st.subheader('UZT guest info')
col5, col6, col7, col8  = st.columns([1.5,1,1,1.5])

guest1_list = []
guest2_list = []
guest3_list = []
guest4_list = []
guest5_list = []

with col5:
    # st.text('게스트 입력')
    title1 = st.text_input(label='게스트1', placeholder='게스트 이름 입력',label_visibility='collapsed'),
    title2 = st.text_input(label='게스트2', placeholder='게스트 이름 입력',label_visibility='collapsed'),
    title3 = st.text_input(label='게스트3', placeholder='게스트 이름 입력',label_visibility='collapsed'),
    title4 = st.text_input(label='게스트4', placeholder='게스트 이름 입력',label_visibility='collapsed'),
    title5 = st.text_input(label='게스트5', placeholder='게스트 이름 입력',label_visibility='collapsed'),
with col6:
    # st.text('성별')
    sex_option = ['성별','남','여']
    option1= st.selectbox('성별1',sex_option, placeholder="성별선택",label_visibility='collapsed')
    option2= st.selectbox('성별2',sex_option, placeholder='성별선택',label_visibility='collapsed')
    option3= st.selectbox('성별3',sex_option, placeholder='성별선택',label_visibility='collapsed')
    option4= st.selectbox('성별4',sex_option, placeholder='성별선택',label_visibility='collapsed')
    option5= st.selectbox('성별5',sex_option, placeholder='성별선택',label_visibility='collapsed')
with col7:
    # st.text('Ntrp') 
    Ntrp_option = ['<Ntrp>','2.0','2.5','3.0','3.5','4.0','4.5']
    Ntrp_option1 = st.selectbox('Ntrp1', Ntrp_option, placeholder='Choose an Ntrp',label_visibility='collapsed')
    Ntrp_option2 = st.selectbox('Ntrp2', Ntrp_option, placeholder='Choose an Ntrp',label_visibility='collapsed')
    Ntrp_option3 = st.selectbox('Ntrp3', Ntrp_option, placeholder='Choose an Ntrp',label_visibility='collapsed')
    Ntrp_option4 = st.selectbox('Ntrp4', Ntrp_option, placeholder='Choose an Ntrp',label_visibility='collapsed')
    Ntrp_option5 = st.selectbox('Ntrp5', Ntrp_option, placeholder='Choose an Ntrp',label_visibility='collapsed')
with col8: 
    # st.text('등록 상태')
    
    if (len(title1[0]) >= 1 and option1 == '남' and Ntrp_option1 != '<Ntrp>'):
        team_list.append([title1[0], 'M', float(Ntrp_option1)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if (len(title1[0]) >= 1 and option1 == '여' and Ntrp_option1 != '<Ntrp>'):
        team_list.append([title1[0], 'F', float(Ntrp_option1)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if len(title1[0]) == 0 or option1 == '성별' or Ntrp_option1 == '<Ntrp>':
        st.write(":angry: **:red[게스트정보 부족]**")

    if (len(title2[0]) >= 1 and option2 == '남' and Ntrp_option2 != '<Ntrp>'):
        team_list.append([title2[0], 'M', float(Ntrp_option2)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if (len(title2[0]) >= 1 and option2 == '여' and Ntrp_option2 != '<Ntrp>'):
        team_list.append([title2[0], 'F', float(Ntrp_option2)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if len(title2[0]) == 0 or option2 == '성별' or Ntrp_option2 == '<Ntrp>':
        st.write(":angry: **:red[게스트정보 부족]**")

    if (len(title3[0]) >= 1 and option3 == '남' and Ntrp_option3 != '<Ntrp>'):
        team_list.append([title3[0], 'M', float(Ntrp_option3)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if (len(title3[0]) >= 1 and option3 == '여' and Ntrp_option3 != '<Ntrp>'):
        team_list.append([title3[0], 'F', float(Ntrp_option3)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if len(title3[0]) == 0 or option3 == '성별' or Ntrp_option3 == '<Ntrp>':
        st.write(":angry: **:red[게스트정보 부족]**")

    if (len(title4[0]) >= 1 and option4 == '남' and Ntrp_option4 != '<Ntrp>'):
        team_list.append([title4[0], 'M', float(Ntrp_option4)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if (len(title4[0]) >= 1 and option4 == '여' and Ntrp_option4 != '<Ntrp>'):
        team_list.append([title4[0], 'F', float(Ntrp_option4)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if len(title4[0]) == 0 or option4 == '성별' or Ntrp_option4 == '<Ntrp>':
        st.write(":angry: **:red[게스트정보 부족]**")

    if (len(title5[0]) >= 1 and option5 == '남' and Ntrp_option5 != '<Ntrp>'):
        team_list.append([title5[0], 'M', float(Ntrp_option5)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if (len(title5[0]) >= 1 and option5 == '여' and Ntrp_option5 != '<Ntrp>'):
        team_list.append([title5[0], 'F', float(Ntrp_option5)])
        st.write(':smile: **:green[게스트 추가 완료]**')
    if len(title5[0]) == 0 or option5 == '성별' or Ntrp_option5 == '<Ntrp>':
        st.write(":angry: **:red[게스트정보 부족]**")

# st.multiselect('참여자:', team_list, default=list_sum)
# st.write(team_list)
name_list = []

for i in team_list:
    name_list.append(i[0])

st.subheader('Match information')
st.write(f'**총 참여자 수:** {len(name_list)}명 (UZT {cnt}명 & 게스트 수 {len(name_list)-cnt}명)')
st.write(f'**참여자:** {name_list}')
st.write(f' ')

col9, col10, col11, col12, col13, col14 = st.columns([2,2,2,1,1,1])
with col9:
    game_date = st.date_input('경기일자')
with col10:
    start_time = st.time_input('시작시간')
with col11:
    end_time = st.time_input('종료시간')
with col12:
    court1_name = st.text_input('코트번호1', key='court1')
with col13:
    court2_name = st.text_input('코트번호2', key='court2')
with col14:
    court3_name = st.text_input('코트번호3', key='court3')
    # button = st.button('팀조합 생성')

button = st.button('팀조합 생성')

court1_col = court1_name
court2_col = court2_name
court3_col = court3_name

if button:
    if len(team_list) == 12:
        list_sum = team_list

        c_num = 3
        game = 4
        m_cnt = 0
        f_cnt = 0
        m_list = []
        f_list = []

        balance = False

        if len(list_sum) >= 8:
            for i in list_sum:
                if i[1] == 'F':
                    f_cnt += 1
                    f_list.append(i)
                elif i[1] == 'M':
                    m_cnt += 1
                    m_list.append(i)

            while 1:
                total_list = []
                while 1:
                    mix_list = []
                    nt_list_1 = []
                    nt_list_2 = []
                    nt_list_sum = []
                    bal1 = []
                    bal2 = []
                    name = []
                    if balance == False:
                        pass_list = []
                        total_pass_name = []
                        m_list = shuffle(m_list)
                        f_list = shuffle(f_list)
                        mix_list = m_list.copy()
                        for j in range(f_cnt):
                            mix_list.insert(j*2, f_list[j])
                        for k in range(len(mix_list)):
                            if k%2 == 0:
                                nt_list_1.append(mix_list[k][2])
                            if k%2 == 1:
                                nt_list_2.append(mix_list[k][2])
                        bal = [x+y for x,y in zip(nt_list_1, nt_list_2)]
                        for k in range(len(bal)):
                            if k%2 == 0:
                                bal1.append(bal[k])
                            if k%2 == 1:
                                bal2.append(bal[k])
                        bal_minus = [abs(x-y) for x,y in zip(bal1, bal2)]
                        for i in bal_minus:
                            if i < 1:
                                pass_list.append(True)
                            elif i >= 1:
                                pass_list.append(False)
                        if False not in pass_list:
                            total_list.append(mix_list)
                            if len(total_list) == game:
                                total_list_np = np.array(total_list).ravel()
                                for i in range(len(total_list_np)):
                                    if i%3==0:
                                        total_pass_name.append(total_list_np[i])
                                pair = np.array(total_pass_name).reshape((c_num*2*game,2))
                                pair.sort(axis=1)
                                pair_list = pair.tolist()
                                pair_list_convert = [str(i) for i in pair_list]
                                dup_num = max(Counter(pair_list_convert).values())
                                break
                if dup_num == 1:
                    result = pair.reshape((game,-1))
                    if len(result[0]) == 12:
                        df = pd.DataFrame(result)
                        df.columns = ['1','2','3','4','5','6','7','8','9','10','11','12']
                        df['1팀'] = df[['1','2']].apply(" ".join, axis=1)
                        df['2팀'] = df[['3','4']].apply(" ".join, axis=1)
                        df['3팀'] = df[['5','6']].apply(" ".join, axis=1)
                        df['4팀'] = df[['7','8']].apply(" ".join, axis=1)
                        df['5팀'] = df[['9','10']].apply(" ".join, axis=1)
                        df['6팀'] = df[['11','12']].apply(" ".join, axis=1)
                        df2=df[['1팀','2팀','3팀','4팀','5팀','6팀']]
                     
                        df3 = pd.DataFrame(df2.values,
                                        index = df2.index,
                                        columns = [[f'{court1_col}번 코트',f'{court1_col}번 코트',f'{court2_col}번 코트',f'{court2_col}번 코트',f'{court3_col}번 코트',f'{court3_col}번 코트'],['1팀','2팀','3팀','4팀','5팀','6팀']])
                                        # columns = [['1코트','1코트','2코트','2코트','3코트','3코트'],['1팀','2팀','3팀','4팀','5팀','6팀']])
                    break

            st.table(df3)


    elif len(team_list) == 8:
        list_sum = team_list

        c_num = 2
        game = 4
        m_cnt = 0
        f_cnt = 0
        m_list = []
        f_list = []

        balance = False

        if len(list_sum) == 8:
            for i in list_sum:
                if i[1] == 'F':
                    f_cnt += 1
                    f_list.append(i)
                elif i[1] == 'M':
                    m_cnt += 1
                    m_list.append(i)

            while 1:
                total_list = []
                while 1:
                    mix_list = []
                    nt_list_1 = []
                    nt_list_2 = []
                    nt_list_sum = []
                    bal1 = []
                    bal2 = []
                    name = []
                    if balance == False:
                        pass_list = []
                        total_pass_name = []
                        m_list = shuffle(m_list)
                        f_list = shuffle(f_list)
                        mix_list = m_list.copy()
                        for j in range(f_cnt):
                            mix_list.insert(j*2, f_list[j])
                        for k in range(len(mix_list)):
                            if k%2 == 0:
                                nt_list_1.append(mix_list[k][2])
                            if k%2 == 1:
                                nt_list_2.append(mix_list[k][2])
                        bal = [x+y for x,y in zip(nt_list_1, nt_list_2)]
                        for k in range(len(bal)):
                            if k%2 == 0:
                                bal1.append(bal[k])
                            if k%2 == 1:
                                bal2.append(bal[k])
                        bal_minus = [abs(x-y) for x,y in zip(bal1, bal2)]
                        for i in bal_minus:
                            if i < 1:
                                pass_list.append(True)
                            elif i >= 1:
                                pass_list.append(False)
                        if False not in pass_list:
                            total_list.append(mix_list)
                            if len(total_list) == game:
                                total_list_np = np.array(total_list).ravel()
                                for i in range(len(total_list_np)):
                                    if i%3==0:
                                        total_pass_name.append(total_list_np[i])
                                pair = np.array(total_pass_name).reshape((c_num*2*game,2))
                                pair.sort(axis=1)
                                pair_list = pair.tolist()
                                pair_list_convert = [str(i) for i in pair_list]
                                dup_num = max(Counter(pair_list_convert).values())
                                break
                if dup_num == 1:
                    result = pair.reshape((game,-1))
                    if len(result[0]) == 8:
                        df = pd.DataFrame(result)
                        df.columns = ['1','2','3','4','5','6','7','8']
                        df['1팀'] = df[['1','2']].apply(" ".join, axis=1)
                        df['2팀'] = df[['3','4']].apply(" ".join, axis=1)
                        df['3팀'] = df[['5','6']].apply(" ".join, axis=1)
                        df['4팀'] = df[['7','8']].apply(" ".join, axis=1)
                        df2=df[['1팀','2팀','3팀','4팀']]
                        df3 = pd.DataFrame(df2.values,
                                        index = df2.index,
                                        columns = [[f'{court1_col} court',f'{court1_col} court',f'{court2_col} court',f'{court2_col} court'],['1팀','2팀','3팀','4팀']])
                    break

            st.table(df3)

    elif len(team_list) != 12 or len(team_list) != 8:
        st.write('8명이나 12명으로 채워주세요!')

    # elif len(team_list) != 8:
    #     st.write('8명이나 12명을 채우시오!')


