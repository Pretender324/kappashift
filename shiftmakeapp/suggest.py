import pandas as pd
from django_pandas.io import read_frame
from .models import EntryModel
from datetime import *


class Suggest():

    def __init__(self, object_list, freshman, competition, before, after):
        self.competition = competition

        df = read_frame(object_list)
        df = pd.concat([df, pd.DataFrame(columns=freshman)])
        print(df)
        for i in range(len(df)):
            df.iloc[i, 3] = datetime.strptime(
                str(df.iloc[i, 3]), '%H:%M:%S')
            print(type(df.iloc[i, 3]))
        self.id_list = list(df["id"])
        self.df = df.set_index("id")

        for member in freshman:
            self.fillInBeforeEvent(member, before)
            self.fillInAfterEvent(member, after)

        print(self.df)

    def fillInBeforeEvent(self, member, n):
        """
        memberの種目前n分を埋める
        """
        entries = EntryModel.objects.filter(
            member=member, shift__in=self.competition.shift.all())
        name = member.last_name + member.first_name
        for entry in entries:
            p = entry.shift
            t = datetime.strptime(
                str(p.start_time), '%H:%M:%S')
            i = self.id_list.index(p.id)
            tb = t
            while t - tb <= timedelta(minutes=n):
                self.df.loc[self.id_list[i], name] = 1
                if i > 0:
                    i -= 1
                    tb = self.df.loc[self.id_list[i], "start_time"]
                else:
                    break

    def fillInAfterEvent(self, member, n):
        """
        memberの種目後n分を埋める
        """
        entries = EntryModel.objects.filter(
            member=member, shift__in=self.competition.shift.all())
        name = member.last_name + member.first_name
        for entry in entries:
            p = entry.shift
            t = datetime.strptime(
                str(p.start_time), '%H:%M:%S')
            i = self.id_list.index(p.id)
            ta = t
            while ta - t <= timedelta(minutes=n):
                self.df.loc[self.id_list[i], name] = 1
                if i < len(self.id_list) - 1:
                    i += 1
                    ta = self.df.loc[self.id_list[i], "start_time"]
                else:
                    break
