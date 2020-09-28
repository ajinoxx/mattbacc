import discord
from discord.ext import tasks, commands
import time
import datetime

#TODO
# Make the loop wait the remainder time, starting the loop at 00 seconds

class bellSch(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.tServerID = 543185885232103434 #Big brainus
        self.tChannelID = 756194795411603547 #bells
        self.tRoleID = 756238148404510802
        self.myID = 191334024612937729
        self.holidays = ['09/28', '10/12', '11/11', '11/26', '11/27']
        self.timeChecker.start()


    def checkHoliday(self, dateTC):
        print('checkHoliday was called')
        isHoliday = False
        for d in self.holidays:
            if str(dateTC) == d:
                isHoliday = True
                break
        return isHoliday

    @commands.Cog.listener()
    async def on_ready(self):
        print('SchBot ready')

    @commands.command(aliases=['sch', 'sched'])
    async def schedule(self, ctx):
        userDM = ctx.author.dm_channel
        if userDM == None:
            userDM = await ctx.author.create_dm()
        await userDM.send("**Bell Schedule:** ```Period 1: 07:28-08:08\n\nHomeroom: 08:08-08:13\n\nPeriod 2: 08:17-08:57\n\nPeriod 3: 09:01-09:41\n\nPeriod 4: 09:45-10:25\n\nPeriod 5: 10:29-11:09\n\nPeriod 6: 11:13-11:53\n\nPeriod 7: 11:57-12:37\n\nPeriod 8: 12:41-01:21\n\nPeriod 9: 01:25-02:05```")
        await ctx.send('Sent you a schedule! Check your DMs.')

    @commands.command(aliases=['ah', 'aholiday'])
    async def addholiday(self, ctx, date=''):
        if ctx.author.id == self.myID:
            if date != '' and len(str(date)) == 5 and str(date)[2] == '/':
                self.holidays.append(str(date))
                await ctx.send(f'Added holiday, {date}!')
                self.holidays.sort()
            else:
                await ctx.send('Please input a proper date.')

    @commands.command(aliases=['rh', 'rholiday'])
    async def removeholiday(self, ctx, date=''):
        if ctx.author.id == self.myID:
            hasDate = False
            for d in self.holidays:
                if date == d:
                    hasDate = True
                    break
            if hasDate == True:
                self.holidays.remove(date)
                await ctx.send(f'{date} has been removed from the array.')
                self.holidays.sort()
            else:
                await ctx.send(f'{date} is not in the array!')

    @commands.command(aliases=['hl', 'lholiday', 'lh'])
    async def holidaylist(self, ctx):
        self.holidays.sort()
        msgTS = ''
        for d in self.holidays:
            msgTS += d + ' '
        await ctx.send(f'The holidays I have are:\n{msgTS}')

    @tasks.loop(seconds=60, count=None, reconnect=True)
    async def timeChecker(self):
        dayOfWeek = datetime.date.today().weekday()
        currentTime = datetime.datetime.now().strftime('%H:%M')
        currentSec = datetime.datetime.now().strftime('%S')
        currentDate = datetime.datetime.now().strftime('%m/%d')

        tServer = self.client.get_guild(self.tServerID)
        tChannel = tServer.get_channel(self.tChannelID)
        tRole = tServer.get_role(self.tRoleID)

        isaHoliday = self.checkHoliday(currentDate)

        print(f'isaHoliday = {isaHoliday} with the date of {currentDate}')

        #if dayOfWeek == 5 or dayOfWeek == 6 or isaHoliday:#lambda d: d == currentDate, holidays:
        #    self.bellSch.cancel()
        #    print('The loop was canceled.')
        
        if dayOfWeek != 5 and dayOfWeek != 6 and not isaHoliday:
            print('The loop was not canceled.')
            print("It's a day of the week")
            print(f"It's {currentSec} into the minute")

            if currentTime == '07:23':
                print('Period 1 starts in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 1 starts in 5 minutes!')
            elif currentTime == '07:28':
                print('Period 1 has started!')
                await tChannel.send(f'{tRole.mention} Period 1 has started!')
            elif currentTime == '08:03':
                print('Period 1 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 1 ends in 5 minutes!')
            elif currentTime == '08:08':
                print('Period 1 has ended!')
                await tChannel.send(f'{tRole.mention} Period 1 has ended!')
            
            elif currentTime == '08:12':
                print('Period 2 starts in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 2 starts in 5 minutes!')
            elif currentTime == '08:17':
                print('Period 2 has started!')
                await tChannel.send(f'{tRole.mention} Period 2 has started!')
            elif currentTime == '08:52':
                print('Period 2 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 2 ends in 5 minutes!')
            elif currentTime == '08:57':
                print('Period 2 has ended!')
                await tChannel.send(f'{tRole.mention} Period 2 has ended!')
            
            elif currentTime == '09:01':
                print('Period 3 has started!')
                await tChannel.send(f'{tRole.mention} Period 3 has started!')
            elif currentTime == '09:36':
                print('Period 3 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 3 ends in 5 minutes!')
            elif currentTime == '09:41':
                print('Period 3 has ended!')
                await tChannel.send(f'{tRole.mention} Period 3 has ended!')            
            
            elif currentTime == '09:45':
                print('Period 4 has started!')
                await tChannel.send(f'{tRole.mention} Period 4 has started!')
            elif currentTime == '10:20':
                print('Period 4 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 4 ends in 5 minutes!')
            elif currentTime == '10:25':
                print('Period 4 has ended!')
                await tChannel.send(f'{tRole.mention} Period 4 has ended!')
            
            elif currentTime == '10:29':
                print('Period 5 has started!')
                await tChannel.send(f'{tRole.mention} Period 5 has started!')
            elif currentTime == '11:04':
                print('Period 5 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 5 ends in 5 minutes!')
            elif currentTime == '11:09':
                print('Period 5 has ended!')
                await tChannel.send(f'{tRole.mention} Period 5 has ended!')
            
            elif currentTime == '11:13':
                print('Period 6 has started!')
                await tChannel.send(f'{tRole.mention} Period 6 has started!')
            elif currentTime == '11:48':
                print('Period 6 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 6 ends in 5 minutes!')
            elif currentTime == '11:53':
                print('Period 6 has ended!')
                await tChannel.send(f'{tRole.mention} Period 6 has ended!')

            elif currentTime == '11:57':
                print('Period 7 has started!')
                await tChannel.send(f'{tRole.mention} Period 7 has started!')
            elif currentTime == '12:32':
                print('Period 7 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 7 ends in 5 minutes!')
            elif currentTime == '12:37':
                print('Period 7 has ended!')
                await tChannel.send(f'{tRole.mention} Period 7 has ended!')

            elif currentTime == '12:41':
                print('Period 8 has started!')
                await tChannel.send(f'{tRole.mention} Period 8 has started!')
            elif currentTime == '13:16':
                print('Period 8 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 8 ends in 5 minutes!')
            elif currentTime == '13:21':
                print('Period 8 has ended!')
                await tChannel.send(f'{tRole.mention} Period 8 has ended!')

            elif currentTime == '13:25':
                print('Period 9 has started!')
                await tChannel.send(f'{tRole.mention} Period 9 has started!')
            elif currentTime == '14:00':
                print('Period 9 ends in 5 minutes!')
                await tChannel.send(f'{tRole.mention} Period 9 ends in 5 minutes!')
            elif currentTime == '14:05':
                print('Period 9 has ended!')
                await tChannel.send(f'{tRole.mention} Period 9 has ended!')
            
    @timeChecker.before_loop
    async def before_timeChecker(self):
        print('Waiting for bot to start')
        await self.client.wait_until_ready()
        print('Bot is ready, starting loop')
    
def setup(client):
    client.add_cog(bellSch(client))