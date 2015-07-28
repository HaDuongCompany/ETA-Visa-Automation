set logdir=E:\NTTICT_TestTool\ProjectVisa\reports\%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
mkdir %logdir%

:: run the automation script
call python -m robot.run --variablefile D:\ETA\resources\variables\MEAU_test_variable.py --outputdir %logdir% --suite * D:\ETA\suites
