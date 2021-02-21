# hack-program

an example Python CLI program

## Confirm appointment package

This package gives a patient an appointment date and time and asks them to confirm or cancel the appointment.

The package takes three inputs: YES, NO, or STOP (to stop receiving appointment reminders).

The appointment time currently is randomly generated for this year between 9-5. 

In the future it might get input from doctor's office for patient appoitnment information, and then based on patient identity query their phone number to send them this reminder.

## User manual

To get help for which commands in the program do what, run this:
```bash
confirm_appointment -h
```

```bash
usage: confirm_appointment [-h] [--YES] [--NO] [--STOP]

optional arguments:
  -h, --help  show this help message and exit
  --YES       confirm appointment
  --NO        cancel appointment
  --STOP      Stop receiving messages about appointment 
```

