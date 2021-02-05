//Find
			Set(HEADER_GC_DEAD,					CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCDead), STATIC_SIZE_PACKET));
			
///Add
#if defined(GUILD_RANK_SYSTEM)
			Set(HEADER_GC_GUILD_RANKING, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCGuildRankingSend), STATIC_SIZE_PACKET));
#endif