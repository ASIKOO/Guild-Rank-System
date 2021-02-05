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
	HEADER_GC_GUILD_RANKING = 161,
};
typedef struct packet_guild_ranking_send
{
	BYTE	header;
	BYTE	subheader;
	int	id;
	char	szGuildName[GUILD_NAME_MAX_LEN + 1];
	char	szOwnerName[CHARACTER_NAME_MAX_LEN + 1];
	int	level;
	int	point;
	int	win;
	int draw;
	int loss;
} TPacketGCGuildRankingSend;
#endif