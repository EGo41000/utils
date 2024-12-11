import pydantic, datetime

class Event(pydantic.BaseModel):
    SUMMARY: str
    DESCRIPTION: str
    DTSTART: datetime.datetime
    DTEND: datetime.datetime
    LOCATION: str = ''

    @classmethod
    def ical_start(cls, name:str):
        print(f'''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//{name}// 2.20.2//
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:{name} {datetime.datetime.now().strftime('%Y%m%d %H%M%S')}
X-WR-CALDESC:Planning {name}
X-WR-TIMEZONE:Europe/Paris''')

    @classmethod
    def ical_end(cls):
        print(f'''END:VCALENDAR''')

    def vevent(self):
        n=70
        summary='SUMMARY:'+self.SUMMARY.replace('\n', '\\n')
        summary="\n ".join([summary[i:i+n] for i in range(0, len(summary), n)])
        desc="DESCRIPTION:"+self.DESCRIPTION.replace('\n', '\\n')
        desc="\n ".join([desc[i:i+n] for i in range(0, len(desc), n)])
        return f"""BEGIN:VEVENT
UID:{self.DTSTART}-{datetime.datetime.now().strftime('%Y%m%dT%H%M%S')}-@calendar
DTSTAMP:{datetime.datetime.now().strftime('%Y%m%dT%H%M%S')}
{desc}
DTSTART:{self.DTSTART.strftime('%Y%m%d')}
DTEND:{self.DTEND.strftime('%Y%m%d')}
LOCATION:{self.LOCATION}
{summary}
END:VEVENT"""
