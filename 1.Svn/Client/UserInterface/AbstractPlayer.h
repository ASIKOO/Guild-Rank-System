//Find
virtual const char* GetName() = 0;

///Add

#if defined(GUILD_RANK_SYSTEM)
		virtual DWORD		GetGuildID() = 0;
#endif