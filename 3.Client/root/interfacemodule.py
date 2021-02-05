#Add
if app.GUILD_RANK_SYSTEM:
	import uiGuildRanking
	
#Find
		self.wndChatLog = wndChatLog
		
#Add
		if app.GUILD_RANK_SYSTEM:
			self.wndGuildRanking = uiGuildRanking.GuildRankingDialog()
			
#Find
		if self.wndSafebox:
			self.wndSafebox.Destroy()
			
#Add
		if app.GUILD_RANK_SYSTEM:
			if self.wndGuildRanking:
				self.wndGuildRanking.Destory()
				
#Find
		del self.wndItemSelect
		
#Add
		if app.GUILD_RANK_SYSTEM:
			del self.wndGuildRanking
			
#Find
	def RefreshSafebox(self):
		self.wndSafebox.RefreshSafebox()
		
#Add
	if app.GUILD_RANK_SYSTEM:
		def OpenGuildRanking(self):
			self.wndGuildRanking.Open()