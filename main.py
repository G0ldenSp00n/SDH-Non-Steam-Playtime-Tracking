class Plugin:
    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def add(self, left, right):
        return left + right


    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        await pluginManagerUtrils.execture_in_tab("SP", false,f"""
                (fuction() {{
                    const nonSteamApps = [];
                    for (const [i, app] of window.appStore.m_mapApps._data) {
                        if (app.value.app_type === 1073741824) {
                            nonSteamApps.push(app);
                        }
                    }

                    for (const [i, nonSteamApp] of nonSteamApps) {
                        nonSteamApp.value.minutes_playtime_forever = 345;
                    }
                }})()
                """ )
        pass
