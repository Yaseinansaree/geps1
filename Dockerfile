FRom python:latest
COPY bot.py .
COPY help.txt .
COPY help1.txt .
COPY help2.txt .
COPY help3.txt .
COPY farsi-dic.json .
COPY dontReadMe.txt .
COPY qrozAdmins.txt .
COPY api_rubika.py .
RUN pip3 install rubika --upgrade
RUN pip install gtts
RUN pip install requests
RUN pip install pillow
RUN pip install pycryptodome==3.10.1
RUN pip install arabic-reshaper
RUN pip install python-bidi
RUN pip install mutagen
RUN pip install googletrans==3.1.0a0
ENTRYPOINT [ "python3" ]
CMD ["bot.py"]