quest guild_ranking begin
	state start begin	
		when 9006.chat."Guild Rank List" begin
			setskin(NOWINDOW)
			pc.open_guild_ranking()
		end
	end
end