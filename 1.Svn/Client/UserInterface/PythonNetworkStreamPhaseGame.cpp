//Find
			case HEADER_GC_EXCHANGE:
				ret = RecvExchangePacket();
				break;
				
///Add
#if defined(GUILD_RANK_SYSTEM)
			case HEADER_GC_GUILD_RANKING:
				ret = RecvGuildRanking();
				break;
#endif

//Find
void CPythonNetworkStream::ToggleGameDebugInfo()
{
	...
}

///Add
#if defined(GUILD_RANK_SYSTEM)
bool CPythonNetworkStream::RecvGuildRanking()
{
	TPacketGCGuildRankingSend Packet;
	if (!Recv(sizeof(Packet), &Packet)) {
		Tracen("RecvGuildRanking Error");
		return false;
	}

	switch (Packet.subheader)
	{
	case GUILD_RANK::SUBHEADER_GUILD_RANKING_SEND:
		CPythonGuildRanking::Instance().RegisterRankingData(Packet.id, Packet.szGuildName, Packet.szOwnerName, Packet.level, Packet.point, Packet.win, Packet.draw, Packet.loss);
		break;
	case GUILD_RANK::SUBHEADER_GUILD_RANKING_OPEN:
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_GUILD_RANK_OPEN", Py_BuildValue("()"));
		break;
	}

	return true;
}
#endif