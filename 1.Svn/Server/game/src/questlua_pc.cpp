//Find
	int pc_get_dx( lua_State* L )
	{
		...
	}
	
///Add
#if defined(GUILD_RANK_SYSTEM)
	int32_t pc_open_guild_ranking(lua_State* L)
	{
		LPCHARACTER pkChar = CQuestManager::instance().GetCurrentCharacterPtr();
		if (!pkChar || !pkChar->GetDesc())
			return 0;

		std::unique_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT guild.id, guild.name AS guild_name, player.name AS guild_owner, guild.level, guild.win, guild.draw, guild.loss, guild.ladder_point FROM player.guild INNER JOIN player.player ON player.id = guild.master ORDER BY guild.level DESC, guild.win DESC, guild.draw DESC, guild.ladder_point DESC, guild.loss DESC LIMIT %d", GUILD_RANK::GUILD_RANKING_MAX_NUM));
		if (pMsg->uiSQLErrno)
			return 0;

		MYSQL_ROW row;
		while ((row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
		{
			const int32_t ID = std::stoi(row[0]);
			const char* GuildName = row[1];
			const char* OwnerName = row[2];
			const int32_t Level = std::stoi(row[3]);
			const int32_t Win = std::stoi(row[4]);
			const int32_t Draw = std::stoi(row[5]);
			const int32_t Loss = std::stoi(row[6]);
			const int32_t Point = std::stoi(row[7]);

			const TPacketGCGuildRankingSend t = TPacketGCGuildRankingSend(ID, GuildName, OwnerName, Level, Point, Win, Draw, Loss);
			pkChar->GetDesc()->Packet(&t, sizeof(t));
		}

		const TPacketGCGuildRankingSend t = TPacketGCGuildRankingSend();
		pkChar->GetDesc()->Packet(&t, sizeof(t));

		return 0;
	}
#endif

//Find
			{ "can_warp",			pc_can_warp		},
			
///Add
#if defined(GUILD_RANK_SYSTEM)
			{ "open_guild_ranking", pc_open_guild_ranking },
#endif