//Find
typedef struct packet_dead
{
	...
} TPacketGCDead;

///Add
#if defined(GUILD_RANK_SYSTEM)
enum GUILD_RANK
{
	SUBHEADER_GUILD_RANKING_SEND,
	SUBHEADER_GUILD_RANKING_OPEN,
	GUILD_RANKING_MAX_NUM = 100,
	HEADER_GC_GUILD_RANKING = 161,
};
typedef struct packet_guild_ranking_send
{
	packet_guild_ranking_send()
	{
		std::strncpy(szOwnerName, "", sizeof(szOwnerName));
		std::strncpy(szGuildName, "", sizeof(szGuildName));
	}
	packet_guild_ranking_send(int32_t c_id, const char* c_guild, const char* c_name, int32_t c_level, int32_t c_point, int32_t c_win, int32_t c_draw, int32_t c_loss)
		: subheader(GUILD_RANK::SUBHEADER_GUILD_RANKING_SEND), id(c_id), level(c_level), point(c_point), win(c_win), draw(c_draw), loss(c_loss)
	{
		std::strncpy(szOwnerName, c_name, sizeof(szOwnerName));
		std::strncpy(szGuildName, c_guild, sizeof(szGuildName));
	}
	uint8_t	header = HEADER_GC_GUILD_RANKING;
	uint8_t	subheader = SUBHEADER_GUILD_RANKING_OPEN;
	int32_t		id = 0;
	char	szGuildName[GUILD_NAME_MAX_LEN + 1];
	char	szOwnerName[CHARACTER_NAME_MAX_LEN + 1];
	int32_t		level = 0;
	int32_t		point = 0;
	int32_t		win = 0;
	int32_t		draw = 0;
	int32_t		loss = 0;
} TPacketGCGuildRankingSend;
#endif