//Find
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

///Add
#if defined(GUILD_RANK_SYSTEM)
	PyModule_AddIntConstant(poModule, "GUILD_RANK_SYSTEM", true);
#else
	PyModule_AddIntConstant(poModule, "GUILD_RANK_SYSTEM", false);
#endif