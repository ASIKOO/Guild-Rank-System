import uiScriptLocale
BACK_IMG_PATH = "d:/ymir work/ui/public/public_board_back/"
ROOT_PATH = "d:/ymir work/ui/game/guild/guildrankingsystem/"
BOARD_WIDTH = 535
BOARD_HEIGHT = 373
window = {
	"name" : "GuildRankingListWindow",
	"x" : 0,
	"y" : 0,
	"style" : ("movable", "float",),
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 6,
					"y" : 6,
					"width" : BOARD_WIDTH-15,
					"color" : "yellow",
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":BOARD_WIDTH/2, "y":3, "text":uiScriptLocale.GUILD_RANKING_TITLE, "text_horizontal_align":"center" },
					),
				},





				{
					"name" : "LeftTop",
					"type" : "image",
					"x" : 17,
					"y" : 38-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxlefttop.sub",
				},
				{
					"name" : "RightTop",
					"type" : "image",
					"x" : 484,
					"y" : 38-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxrighttop.sub",
				},
				{
					"name" : "LeftBottom",
					"type" : "image",
					"x" : 17,
					"y" : 173+118-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxleftbottom.sub",
				},
				{
					"name" : "RightBottom",
					"type" : "image",
					"x" : 484,
					"y" : 173+118-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxrightbottom.sub",
				},











				{
					"name" : "leftcenterImg",
					"type" : "expanded_image",
					"x" : 17,
					"y" : 38+16-5,
					"image" : BACK_IMG_PATH+"boardback_leftcenterImg.tga",
					"rect" : (0.0, 0.0, 0, 13),
				},
				{
					"name" : "rightcenterImg",
					"type" : "expanded_image",
					"x" : 483,
					"y" : 38+16-5,
					"image" : BACK_IMG_PATH+"boardback_rightcenterImg.tga",
					"rect" : (0.0, 0.0, 0, 13),
				},
				{
					"name" : "topcenterImg",
					"type" : "expanded_image",
					"x" : 17+15,
					"y" :  38-5,
					"image" : BACK_IMG_PATH+"boardback_topcenterImg.tga",
					"rect" : (0.0, 0.0, 26, 0),
				},
				{
					"name" : "bottomcenterImg",
					"type" : "expanded_image",
					"x" : 17+15,
					"y" : 173+118-5,
					"image" : BACK_IMG_PATH+"boardback_bottomcenterImg.tga",
					"rect" : (0.0, 0.0, 26, 0),
				},
				{
					"name" : "centerImg",
					"type" : "expanded_image",
					"x" : 17+15,
					"y" : 38+15-5,
					"image" : BACK_IMG_PATH+"boardback_centerImg.tga",
					"rect" : (0.0, 0.0, 26, 13),
				},








				{
					"name" : "LeftTopSelf",
					"type" : "image",
					"x" : 17,
					"y" : 190+120-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxlefttop.sub",
				},
				{
					"name" : "RightTopSelf",
					"type" : "image",
					"x" : 484,
					"y" : 190+120-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxrighttop.sub",
				},
				{
					"name" : "LeftBottomSelf",
					"type" : "image",
					"x" : 17,
					"y" : 190+15+120-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxleftbottom.sub",
				},
				{
					"name" : "RightBottomSelf",
					"type" : "image",
					"x" : 484,
					"y" : 190+15+120-5,
					"image" : BACK_IMG_PATH+"boardback_mainboxrightbottom.sub",
				},






				{
					"name" : "topcenterImgSelf",
					"type" : "expanded_image",
					"x" : 17+15,
					"y" :  190+120-5,
					"image" : BACK_IMG_PATH+"boardback_topcenterImg.tga",
					"rect" : (0.0, 0.0, 26, 0),
				},
				{
					"name" : "bottomcenterImgSelf",
					"type" : "expanded_image",
					"x" : 17+15,
					"y" : 190+15+120-5,
					"image" : BACK_IMG_PATH+"boardback_bottomcenterImg.tga",
					"rect" : (0.0, 0.0, 26, 0),
				},





				{
					"name" : "GuildTiTleImg",
					"type" : "image",
					"x" : 20,
					"y" : 41-5,
					"image" : ROOT_PATH+"ranking_list_menu.sub",
					"children" :
					(
						{ "name" : "ResultNameRanking", "type" : "text", "x" : 19, "y" : 4,  "text" : uiScriptLocale.GUILD_RANKING_COUNT, },
						{ "name" : "ResultGuildName", "type" : "text", "x" : 75, "y" : 4, "text" : uiScriptLocale.GUILD_GUILD_NAME, },
						{ "name" : "ResultOwnerName", "type" : "text", "x" : 175, "y" : 4, "text" : uiScriptLocale.GUIlD_OWNER_NAME, },
						{ "name" : "ResultLevel", "type" : "text", "x" : 250, "y" : 4, "text" : uiScriptLocale.GUILD_LEVEL, },
						{ "name" : "ResultPoint", "type" : "text", "x" : 295, "y" : 4, "text" : uiScriptLocale.GUILD_POINT, },
						{ "name" : "ResultWin", "type" : "text", "x" : 365, "y" : 4, "text" : uiScriptLocale.GUILD_WIN, },
						{ "name" : "ResultDraw", "type" : "text", "x" : 408, "y" : 4, "text" : uiScriptLocale.GUILD_DRAW, },
						{ "name" : "ResultLoss", "type" : "text", "x" : 449, "y" : 4, "text" : uiScriptLocale.GUILD_LOSS, },
					),
				},
				{
					"name" : "prev_button",
					"type" : "button",
					"x" : (BOARD_WIDTH/2)-(25/2)-12,
					"y" : 345,
					"default_image" : "d:/ymir work/ui/public/public_page_button/page_prev_btn_01.sub",
					"over_image" : "d:/ymir work/ui/public/public_page_button/page_prev_btn_02.sub",
					"down_image" : "d:/ymir work/ui/public/public_page_button/page_prev_btn_01.sub",
				},
				{
					"name" : "prev_first_button",
					"type" : "button",
					"x" : (BOARD_WIDTH/2)-(25/2)-25,
					"y" : 345,
					"default_image" : "d:/ymir work/ui/public/public_page_button/page_first_prev_btn_01.sub",
					"over_image" : "d:/ymir work/ui/public/public_page_button/page_first_prev_btn_02.sub",
					"down_image" : "d:/ymir work/ui/public/public_page_button/page_first_prev_btn_01.sub",
				},
				{
					"name" : "next_button",
					"type" : "button",
					"x" : (BOARD_WIDTH/2)-(25/2)+27,
					"y" : 345,
					"default_image" : "d:/ymir work/ui/public/public_page_button/page_next_btn_01.sub",
					"over_image" : "d:/ymir work/ui/public/public_page_button/page_next_btn_02.sub",
					"down_image" : "d:/ymir work/ui/public/public_page_button/page_next_btn_01.sub",
				},	
				{
					"name" : "next_last_button",
					"type" : "button",
					"x" : (BOARD_WIDTH/2)-(25/2)+25+12,
					"y" : 345,
					"default_image" : "d:/ymir work/ui/public/public_page_button/page_last_next_btn_01.sub",
					"over_image" : "d:/ymir work/ui/public/public_page_button/page_last_next_btn_02.sub",
					"down_image" : "d:/ymir work/ui/public/public_page_button/page_last_next_btn_01.sub",
				},
				{
					"name" : "ScrollBar",
					"type" : "scrollbar",
					"x" : 506,
					"y" : 38,
					"size" : 300,
				},
				{
					"name" : "CurrentPageBack",
					"type" : "thinboard_circle",
					"x" : (BOARD_WIDTH/2)-(25/2),
					"y" : 340,
					"width" : 25,
					"height" : 20,
					"children" :
					(
						{
							"name" : "CurrentPage",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"vertical_align" : "center",
							"horizontal_align" : "center",
							"text_vertical_align" : "center",
							"text_horizontal_align" : "center",
							"text" : "1",
						},
					),
				},				
			),
		},
	),
}