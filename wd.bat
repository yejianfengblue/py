timeout /t 30
cd C:\asktao
for /l %%x in (1, 1, 5) do (
  start "" StartAsktao.exe
  timeout /t 10 /nobreak > NUL
)
exit

