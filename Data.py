# Target Selector modifiers
TARGET_INT_RANGE = {"level"}
TARGET_INT = {"limit"}
TARGET_FLOAT_RANGE = {"x", "y", "z", "x_rotation", "y_rotation", "distance", "dx", "dy", "dz"}
TARGET_USERNAME = {"name", "tag", "team"}
TARGET_GAMEMODE = {"gamemode"}
TARGET_SORT = {"sort"}
TARGET_ENTITY = {"type"}
TARGET_SCORES = {"scores"}
TARGET_ADVANCEMENTS = {"advancements"}
TARGET_NBT = {"nbt"}

TARGET_KEY_LISTS = [TARGET_INT_RANGE,TARGET_INT,TARGET_FLOAT_RANGE,TARGET_USERNAME,TARGET_GAMEMODE,TARGET_SORT,TARGET_ENTITY,TARGET_SCORES,TARGET_ADVANCEMENTS,TARGET_NBT]



# Regular NBT tags
NBT_JSON_TAGS = {"Text1","Text2","Text3","Text4"}
NBT_BYTE_TAGS = {"Ambient","Amplifier","Angry","AttachFace","auto","BatFlags","Bred","CanBreakDoors","CanPickUpLoot","ChestedHorse","CollarColor","Color","conditionMet","Count","crit","CustomDisplayTile","CustomNameVisible","damage","Data","DropItem","EatingHaystack","Enabled","ExactTeleport","ExplosionRadius","extending","Facing","FallFlying","Flicker","Flight","Fuel","Glowing","Health","HurtEntities","Id","ignited","ignoreEntities","inData","inGround","instabuild","Invisible","Invulnerable","invulnerable","IsBaby","IsChickenJockey","isMovable","IsVillager","ItemRotation","Johnny","Leashed","LeftHanded","LightPopulated","map_tracking_position","Marker","mayBuild","mayfly","NoAI","NoBasePlate","NoGravity","note","OnGround","Peek","PersistenceRequired","pickup","player","PlayerCreated","PlayerSpawned","powered","Pumpkin","rewardExp","Rot","Saddle","seenCredits","shake","Sheared","ShowArms","ShowBottom","ShowParticles","Silent","Sitting","SkeletonTrap","SkullType","Sleeping","Slot","Small","source","SpawnForced","SplashPotion","Tame","TerrainPopulated","TrackOutput","Trail","Type","type","Unbreakable", "UpdateLastExecution","V","wasOnGround","Willing","Y"}
NBT_SHORT_TAGS = {"Age","Air","Anger","BurnTime","carried","carriedData","CookTime","CookTimeTotal","DeathTime","Delay","Fire","Fuel","Fuse","Health","HurtTime","life","MaxNearbyEntities","MaxSpawnDelay","MinSpawnDelay","PickupDelay","PotionId","RequiredPlayerRange","SleepTimer","SpawnCount","SpawnRange","Value"}
NBT_INTEGER_TAGS = {"Age","APX","APY","APZ","Base","blockData","blockId","BoundX","BoundY","BoundZ","BrewTime","Career","CareerLevel","CatType","Color","color","ConversionTime","CustomColor","CustomPotionColor","Damage","Data","DataVersion","Dimension","DisabledSlots","DisplayData","DisplayOffset","DragonPhase","Duration","EggLayTime","ExplosionPower","facing","FallHurtMax","foodLevel","foodTickTimer","ForcedAge","Generation","HideFlags","HurtByTimestamp","inLove","Invul","L","Levels","Life","life","LifeTicks","LifeTime","Lifetime","M","map_scale_direction","MapColor","maxUses","MoreCarrotTicks","Operation","OutputSignal","p","ParticleParam1","ParticleParam2","playerGameType","PortalCooldown","posX","posY","posZ","Primary","Profession","RabbitType","ReapplicationDelay","Record","RepairCost","Riches","Score","Secondary","SelectedItemSlot","Size","sizeX","sizeY","sizeZ","SkeletonTrapTime","SpawnX","SpawnY","SpawnZ","SpellTicks","Steps","Strength","SuccessCount","t","Temper","TileID","TileX","TileY","TileZ","Time","TNTFuse","TransferCooldown","uses","Variant","WaitTime","Warmup","Weight","X","x","XpLevel","xPos","XpSeed","XpTotal","xTile","Y","y","yTile","Z","z","zPos","zTile"}
NBT_LONG_TAGS = {"Age","AttachLeast","AttachMost","ConversionPlayerLeast","ConversionPlayerMost","DeathLootTableSeed","InhabitedTime","L","LastExecution","LastUpdate","LootTableSeed","LoveCauseLeast","LoveCauseMost","M","OwnerUUIDLeast","OwnerUUIDMost","UUIDLeast","UUIDMost","XYZ"}
NBT_FLOAT_TAGS = {"0","1","2","3","4","AbsorptionAmount","DurationOnUse","FallDistance","FallHurtAmount","flySpeed","foodExhaustionLevel","foodSaturationLevel","Health","ItemDropChance","progress","Radius","RadiusOnUse","RadiusPerTick","walkSpeed","XpP"}
NBT_DOUBLE_TAGS = {"Amount","Base","damage","PushX","PushZ","rot","TXD","TYD","TZD","x","y","z"}
NBT_STRING_TAGS = {"AffectedBlocksName","AffectedBlocksObjective","AffectedEntitiesName","AffectedEntitiesObjective","AffectedItemsName","AffectedItemsObjective","author","Block","carried","Command","CustomName","DeathLootTable","DisplayTile","HurtBy","i","id","Id","inTile","Item","LastOutput","Lock","LocName","LootTable","metadata","mirror","mode","Motive","Name","name","Owner","ownerName","OwnerUUID","Particle","Pattern","Potion","QueryResultName","QueryResultObjective","rotation","Signature","SuccessCountName","SuccessCountObjective","Team","Thrower","Type","Value"}
NBT_COMPOUND_TAGS = {"0","1","2","3","4","abilities","ArmorItem","BeamTarget","BlockEntityTag","buy","buyB","CanDestroy","CanPlaceOn","CAPE","Colors","CommandStats","Decorations","DecorItem","display","Effects","ench","EnderItems","Entity","EntityTag","ExitPortal","Explosion","Explosions","FadeColors","Fireworks","FireworksItem","Item","Leash","Offers","Owner","Passengers","Patterns","Pose","Potion","Properties","recipeBook","Recipes","RecordItem","RootVehicle","SaddleItem","SelectedItem","sell","ShoulderEntityLeft","ShoulderEntityRight","SKIN","SkullOwner","SpawnData","SpawnPotentials","Tags","Target","Textures","textures","TileEntityData","Value"}
NBT_CUSTOM_COMPOUND_TAGS = {"tag"}

# List tags
NBT_JSON_LIST_TAGS = {"pages"}
NBT_STRING_LIST_TAGS = {"Lore", "Tags","CanDestroy"}
NBT_INTEGER_LIST_TAGS = {"Colors", "FadeColors"}
NBT_FLOAT_LIST_TAGS = {"Body","Head","LeftArm","LeftLeg","Pos","power","RightArm","RightLeg","Rotation"}
NBT_DOUBLE_LIST_TAGS = {"direction","Motion","Power"}
NBT_COMPOUNT_LIST_TAGS = {"ActiveEffects","ArmorItems","AttributeModifiers","Attributes","CustomPotionEffects","HandItems","Inventory","Items","Passengers","StoredEnchantments","textures"}

NBT_KEY_LISTS = [NBT_STRING_LIST_TAGS,NBT_DOUBLE_LIST_TAGS,NBT_INTEGER_LIST_TAGS,NBT_DOUBLE_TAGS,NBT_COMPOUNT_LIST_TAGS,NBT_FLOAT_LIST_TAGS,NBT_FLOAT_TAGS,NBT_LONG_TAGS,NBT_SHORT_TAGS,NBT_STRING_TAGS,NBT_COMPOUND_TAGS,NBT_BYTE_TAGS,NBT_INTEGER_TAGS,NBT_JSON_TAGS,NBT_JSON_LIST_TAGS,NBT_CUSTOM_COMPOUND_TAGS]

# Json keys
JSON_STRING_KEYS = {"text","author","command","insertion","keybind","title","translate"}
JSON_ENTITY_KEYS = {"markerTag","selector"}
JSON_BOOLEAN_KEYS = {"bold","italic","obfuscated","underlined","strikethrough"}
JSON_NESTED_KEYS = {"extra", "with"}

# Some general Minecraft shizzle
PARTICLES = {"ambient_entity_effect","angry_villager","barrier","block","bubble","cloud","crit","damage_indicator","dragon_breath","dripping_lava","dripping_water","dust","effect","elder_guardian","enchanted_hit","enchant","end_rod","entity_effect","explosion_emitter","explosion","falling_dust","firework","fishing","flame","happy_villager","heart","instant_effect","item","item_slime","item_snowball","large_smoke","lava","mycelium","note","poof","portal","rain","smoke","spit","squid_ink","sweep_attack","totem_of_undying","underwater","splash","witch","bubble_pop","current_down","bubble_column_up"}
SOUNDS = {"ambient.cave","ambient.underwater.enter","ambient.underwater.exit","ambient.underwater.loop","ambient.underwater.loop.additions","ambient.underwater.loop.additions.rare","ambient.underwater.loop.additions.ultrarare","block.anvil.break","block.anvil.destroy","block.anvil.fall","block.anvil.hit","block.anvil.land","block.anvil.place","block.anvil.step","block.anvil.use","block.brewing_stand.brew","block.bubble_column.bubble_column_upwards_ambient","block.bubble_column.bubble_pop","block.bubble_column.upwards_inside","block.bubble_column.whirlpool_ambient","block.bubble_column.whirlpool_inside","block.chest.close","block.chest.locked","block.chest.open","block.chorus_flower.death","block.chorus_flower.grow","block.cloth.break","block.cloth.fall","block.cloth.hit","block.cloth.place","block.cloth.step","block.comparator.click","block.dispenser.dispense","block.dispenser.fail","block.dispenser.launch","block.enchantment_table.use","block.end_gateway.spawn","block.end_portal.spawn","block.end_portal_frame.fill","block.enderchest.close","block.enderchest.open","block.fence_gate.close","block.fence_gate.open","block.fire.ambient","block.fire.extinguish","block.furnace.fire_crackle","block.glass.break","block.glass.fall","block.glass.hit","block.glass.place","block.glass.step","block.grass.break","block.grass.fall","block.grass.hit","block.grass.place","block.grass.step","block.gravel.break","block.gravel.fall","block.gravel.hit","block.gravel.place","block.gravel.step","block.iron_door.close","block.iron_door.open","block.iron_trapdoor.close","block.iron_trapdoor.open","block.ladder.break","block.ladder.fall","block.ladder.hit","block.ladder.place","block.ladder.step","block.lava.ambient","block.lava.extinguish","block.lava.pop","block.lever.click","block.metal.break","block.metal.fall","block.metal.hit","block.metal.place","block.metal.step","block.metal_pressureplate.click_off","block.metal_pressureplate.click_on","block.note.basedrum","block.note.bass","block.note.bell","block.note.chime","block.note.flute","block.note.guitar","block.note.harp","block.note.hat","block.note.pling","block.note.snare","block.note.xylophone","block.piston.contract","block.piston.extend","block.portal.ambient","block.portal.travel","block.portal.trigger","block.pumpkin.carve","block.redstone_torch.burnout","block.sand.break","block.sand.fall","block.sand.hit","block.sand.place","block.sand.step","block.shulker_box.close","block.shulker_box.open","block.slime.break","block.slime.fall","block.slime.hit","block.slime.place","block.slime.step","block.snow.break","block.snow.fall","block.snow.hit","block.snow.place","block.snow.step","block.stone.break","block.stone.fall","block.stone.hit","block.stone.place","block.stone.step","block.stone_button.click_off","block.stone_button.click_on","block.stone_pressureplate.click_off","block.stone_pressureplate.click_on","block.tripwire.attach","block.tripwire.click_off","block.tripwire.click_on","block.tripwire.detach","block.water.ambient","block.waterlily.place","block.wood.break","block.wood.fall","block.wood.hit","block.wood.place","block.wood.step","block.wood_button.click_off","block.wood_button.click_on","block.wood_pressureplate.click_off","block.wood_pressureplate.click_on","block.wooden_door.close","block.wooden_door.open","block.wooden_trapdoor.close","block.wooden_trapdoor.open","enchant.thorns.hit","entity.armorstand.break","entity.armorstand.fall","entity.armorstand.hit","entity.armorstand.place","entity.arrow.hit","entity.arrow.hit_player","entity.arrow.shoot","entity.bat.ambient","entity.bat.death","entity.bat.hurt","entity.bat.loop","entity.bat.takeoff","entity.blaze.ambient","entity.blaze.burn","entity.blaze.death","entity.blaze.hurt","entity.blaze.shoot","entity.boat.paddle_land","entity.boat.paddle_water","entity.bobber.retrieve","entity.bobber.splash","entity.bobber.throw","entity.cat.ambient","entity.cat.death","entity.cat.hiss","entity.cat.hurt","entity.cat.purr","entity.cat.purreow","entity.chicken.ambient","entity.chicken.death","entity.chicken.egg","entity.chicken.hurt","entity.chicken.step","entity.cod.ambient","entity.cod.death","entity.cod.flop","entity.cod.hurt","entity.cow.ambient","entity.cow.death","entity.cow.hurt","entity.cow.milk","entity.cow.step","entity.creeper.death","entity.creeper.hurt","entity.creeper.primed","entity.donkey.ambient","entity.donkey.angry","entity.donkey.chest","entity.donkey.death","entity.donkey.hurt","entity.drowned.ambient","entity.drowned.ambient_water","entity.drowned.death","entity.drowned.death_water","entity.drowned.hurt","entity.drowned.hurt_water","entity.drowned.shoot","entity.drowned.step","entity.drowned.swim","entity.egg.throw","entity.elder_guardian.ambient","entity.elder_guardian.ambient_land","entity.elder_guardian.curse","entity.elder_guardian.death","entity.elder_guardian.death_land","entity.elder_guardian.flop","entity.elder_guardian.hurt","entity.elder_guardian.hurt_land","entity.enderdragon.ambient","entity.enderdragon.death","entity.enderdragon.flap","entity.enderdragon.growl","entity.enderdragon.hurt","entity.enderdragon.shoot","entity.enderdragon_fireball.explode","entity.endereye.death","entity.endereye.launch","entity.endermen.ambient","entity.endermen.death","entity.endermen.hurt","entity.endermen.scream","entity.endermen.stare","entity.endermen.teleport","entity.endermite.ambient","entity.endermite.death","entity.endermite.hurt","entity.endermite.step","entity.enderpearl.throw","entity.evocation_fangs.attack","entity.evocation_illager.ambient","entity.evocation_illager.cast_spell","entity.evocation_illager.death","entity.evocation_illager.hurt","entity.evocation_illager.prepare_attack","entity.evocation_illager.prepare_summon","entity.evocation_illager.prepare_wololo","entity.experience_bottle.throw","entity.experience_orb.pickup","entity.firework.blast","entity.firework.blast_far","entity.firework.large_blast","entity.firework.large_blast_far","entity.firework.launch","entity.firework.shoot","entity.firework.twinkle","entity.firework.twinkle_far","entity.fish.swim","entity.generic.big_fall","entity.generic.burn","entity.generic.death","entity.generic.drink","entity.generic.eat","entity.generic.explode","entity.generic.extinguish_fire","entity.generic.hurt","entity.generic.small_fall","entity.generic.splash","entity.generic.swim","entity.ghast.ambient","entity.ghast.death","entity.ghast.hurt","entity.ghast.scream","entity.ghast.shoot","entity.ghast.warn","entity.guardian.ambient","entity.guardian.ambient_land","entity.guardian.attack","entity.guardian.death","entity.guardian.death_land","entity.guardian.flop","entity.guardian.hurt","entity.guardian.hurt_land","entity.horse.ambient","entity.horse.angry","entity.horse.armor","entity.horse.breathe","entity.horse.death","entity.horse.eat","entity.horse.gallop","entity.horse.hurt","entity.horse.jump","entity.horse.land","entity.horse.saddle","entity.horse.step","entity.horse.step_wood","entity.hostile.big_fall","entity.hostile.death","entity.hostile.hurt","entity.hostile.small_fall","entity.hostile.splash","entity.hostile.swim","entity.husk.ambient","entity.husk.death","entity.husk.hurt","entity.husk.step","entity.illusion_illager.ambient","entity.illusion_illager.cast_spell","entity.illusion_illager.death","entity.illusion_illager.hurt","entity.illusion_illager.mirror_move","entity.illusion_illager.prepare_blindness","entity.illusion_illager.prepare_mirror","entity.irongolem.attack","entity.irongolem.death","entity.irongolem.hurt","entity.irongolem.step","entity.item.break","entity.item.pickup","entity.itemframe.add_item","entity.itemframe.break","entity.itemframe.place","entity.itemframe.remove_item","entity.itemframe.rotate_item","entity.leashknot.break","entity.leashknot.place","entity.lightning.impact","entity.lightning.thunder","entity.lingeringpotion.throw","entity.llama.ambient","entity.llama.angry","entity.llama.chest","entity.llama.death","entity.llama.eat","entity.llama.hurt","entity.llama.spit","entity.llama.step","entity.llama.swag","entity.magmacube.death","entity.magmacube.hurt","entity.magmacube.jump","entity.magmacube.squish","entity.minecart.inside","entity.minecart.riding","entity.mooshroom.shear","entity.mule.ambient","entity.mule.chest","entity.mule.death","entity.mule.hurt","entity.painting.break","entity.painting.place","entity.parrot.ambient","entity.parrot.death","entity.parrot.eat","entity.parrot.fly","entity.parrot.hurt","entity.parrot.imitate.blaze","entity.parrot.imitate.creeper","entity.parrot.imitate.elder_guardian","entity.parrot.imitate.enderdragon","entity.parrot.imitate.enderman","entity.parrot.imitate.endermite","entity.parrot.imitate.evocation_illager","entity.parrot.imitate.ghast","entity.parrot.imitate.husk","entity.parrot.imitate.illusion_illager","entity.parrot.imitate.magmacube","entity.parrot.imitate.polar_bear","entity.parrot.imitate.shulker","entity.parrot.imitate.silverfish","entity.parrot.imitate.skeleton","entity.parrot.imitate.slime","entity.parrot.imitate.spider","entity.parrot.imitate.stray","entity.parrot.imitate.vex","entity.parrot.imitate.vindication_illager","entity.parrot.imitate.witch","entity.parrot.imitate.wither","entity.parrot.imitate.wither_skeleton","entity.parrot.imitate.wolf","entity.parrot.imitate.zombie","entity.parrot.imitate.zombie_pigman","entity.parrot.imitate.zombie_villager","entity.parrot.step","entity.phantom.ambient","entity.phantom.bite","entity.phantom.death","entity.phantom.hurt","entity.phantom.swoop","entity.pig.ambient","entity.pig.death","entity.pig.hurt","entity.pig.saddle","entity.pig.step","entity.player.attack.crit","entity.player.attack.knockback","entity.player.attack.nodamage","entity.player.attack.strong","entity.player.attack.sweep","entity.player.attack.weak","entity.player.big_fall","entity.player.breath","entity.player.burp","entity.player.death","entity.player.hurt","entity.player.hurt_drown","entity.player.hurt_on_fire","entity.player.levelup","entity.player.small_fall","entity.player.splash","entity.player.splash.highspeed","entity.player.swim","entity.polar_bear.ambient","entity.polar_bear.baby_ambient","entity.polar_bear.death","entity.polar_bear.hurt","entity.polar_bear.step","entity.polar_bear.warning","entity.puffer_fish.ambient","entity.puffer_fish.blow_out","entity.puffer_fish.blow_up","entity.puffer_fish.death","entity.puffer_fish.flop","entity.puffer_fish.hurt","entity.puffer_fish.sting","entity.rabbit.ambient","entity.rabbit.attack","entity.rabbit.death","entity.rabbit.hurt","entity.rabbit.jump","entity.salmon.ambient","entity.salmon.death","entity.salmon.flop","entity.salmon.hurt","entity.sheep.ambient","entity.sheep.death","entity.sheep.hurt","entity.sheep.shear","entity.sheep.step","entity.shulker.ambient","entity.shulker.close","entity.shulker.death","entity.shulker.hurt","entity.shulker.hurt_closed","entity.shulker.open","entity.shulker.shoot","entity.shulker.teleport","entity.shulker_bullet.hit","entity.shulker_bullet.hurt","entity.silverfish.ambient","entity.silverfish.death","entity.silverfish.hurt","entity.silverfish.step","entity.skeleton.ambient","entity.skeleton.death","entity.skeleton.hurt","entity.skeleton.shoot","entity.skeleton.step","entity.skeleton_horse.ambient","entity.skeleton_horse.death","entity.skeleton_horse.hurt","entity.slime.attack","entity.slime.death","entity.slime.hurt","entity.slime.jump","entity.slime.squish","entity.small_magmacube.death","entity.small_magmacube.hurt","entity.small_magmacube.squish","entity.small_slime.death","entity.small_slime.hurt","entity.small_slime.jump","entity.small_slime.squish","entity.snowball.throw","entity.snowman.ambient","entity.snowman.death","entity.snowman.hurt","entity.snowman.shoot","entity.spider.ambient","entity.spider.death","entity.spider.hurt","entity.spider.step","entity.splash_potion.break","entity.splash_potion.throw","entity.squid.ambient","entity.squid.death","entity.squid.hurt","entity.squid.squirt","entity.stray.ambient","entity.stray.death","entity.stray.hurt","entity.stray.step","entity.tnt.primed","entity.tropical_fish.ambient","entity.tropical_fish.death","entity.tropical_fish.flop","entity.tropical_fish.hurt","entity.turtle.ambient_land","entity.turtle.death","entity.turtle.death_baby","entity.turtle.egg_break","entity.turtle.egg_crack","entity.turtle.egg_hatch","entity.turtle.hurt","entity.turtle.hurt_baby","entity.turtle.lay_egg","entity.turtle.shamble","entity.turtle.shamble_baby","entity.turtle.swim","entity.vex.ambient","entity.vex.charge","entity.vex.death","entity.vex.hurt","entity.villager.ambient","entity.villager.death","entity.villager.hurt","entity.villager.no","entity.villager.trading","entity.villager.yes","entity.vindication_illager.ambient","entity.vindication_illager.death","entity.vindication_illager.hurt","entity.witch.ambient","entity.witch.death","entity.witch.drink","entity.witch.hurt","entity.witch.throw","entity.wither.ambient","entity.wither.break_block","entity.wither.death","entity.wither.hurt","entity.wither.shoot","entity.wither.spawn","entity.wither_skeleton.ambient","entity.wither_skeleton.death","entity.wither_skeleton.hurt","entity.wither_skeleton.step","entity.wolf.ambient","entity.wolf.death","entity.wolf.growl","entity.wolf.howl","entity.wolf.hurt","entity.wolf.pant","entity.wolf.shake","entity.wolf.step","entity.wolf.whine","entity.zombie.ambient","entity.zombie.attack_door_wood","entity.zombie.attack_iron_door","entity.zombie.break_door_wood","entity.zombie.converted_to_drowned","entity.zombie.death","entity.zombie.destroy_egg","entity.zombie.hurt","entity.zombie.infect","entity.zombie.step","entity.zombie_horse.ambient","entity.zombie_horse.death","entity.zombie_horse.hurt","entity.zombie_pig.ambient","entity.zombie_pig.angry","entity.zombie_pig.death","entity.zombie_pig.hurt","entity.zombie_villager.ambient","entity.zombie_villager.converted","entity.zombie_villager.cure","entity.zombie_villager.death","entity.zombie_villager.hurt","entity.zombie_villager.step","item.armor.equip_chain","item.armor.equip_diamond","item.armor.equip_elytra","item.armor.equip_generic","item.armor.equip_gold","item.armor.equip_iron","item.armor.equip_leather","item.armor.equip_turtle","item.axe.strip","item.bottle.empty","item.bottle.fill","item.bottle.fill_dragonbreath","item.bucket.empty","item.bucket.empty_fish","item.bucket.empty_lava","item.bucket.fill","item.bucket.fill_fish","item.bucket.fill_lava","item.chorus_fruit.teleport","item.elytra.flying","item.firecharge.use","item.flintandsteel.use","item.hoe.till","item.shield.block","item.shield.break","item.shovel.flatten","item.totem.use","item.trident.hit","item.trident.hit_ground","item.trident.return","item.trident.riptide_1","item.trident.riptide_2","item.trident.riptide_3","item.trident.throw","item.trident.thunder","music.creative","music.credits","music.dragon","music.end","music.game","music.menu","music.nether","record.11","record.13","record.blocks","record.cat","record.chirp","record.far","record.mall","record.mellohi","record.stal","record.strad","record.wait","record.ward","ui.button.click","ui.toast.challenge_complete","ui.toast.in","ui.toast.out","weather.rain","weather.rain.above"}
POTIONS = {"absorption","blindness","conduit_power","dolphins_grace","fire_resistance","glwoing","haste","health_boost","hunger","instant_damage","instant_health","invisibility","jump_boost","levitation","luck","mining_fatigue","nausea","night_vision","poision","regeneration","resistance","saturation","slow_falling","slowness","speed","strength","unluck","water_breathing","weakness","wither"}
ENTITIES = {"area_effect_cloud","armor_stand","arrow","bat","blaze","boat","cave_spider","chest_minecart","chicken","cod","command_block_minecart","cow","creeper","dolphin","donkey","dragon_fireball","egg","elder_guardian","end_crystal","ender_dragon","ender_pearl","enderman","endermite","evoker","evoker_fangs","experience_bottle","experience_orb","eye_of_ender","falling_block","fireball","firework_rocket","fishing_bobber","furnace_minecart","ghast","giant","guardian","hopper_minecart","horse","husk","illusioner","iron_golem","item","item_frame","leash_knot","lightning_bolt","llama","llama_spit","magma_cube","minecart","mooshroom","mule","ocelot","painting","parrot","pig","player","polar_bear","potion","pufferfish","rabbit","salmon","sheep","shulker","shulker_bullet","silverfish","skeleton","skeleton_horse","slime","small_fireball","snow_golem","snowball","spawner_minecart","spectral_arrow","spider","squid","stray","tnt","tnt_minecart","vex","villager","vindicator","witch","wither","wither_skeleton","wither_skull","wolf","zombie","zombie_horse","zombie_pigman","zombie_villager"}
OBJECTIVE_CRITERIA = {"dummy","trigger","deathCount","playerKillCount","totalKillCount","health","food","air","armor","xp","level","killedByTeam.aqua","killedByTeam.black","killedByTeam.blue","killedByTeam.dark_aqua","killedByTeam.dark_blue","killedByTeam.dark_gray","killedByTeam.dark_green","killedByTeam.dark_purple","killedByTeam.dark_red","killedByTeam.gold","killedByTeam.gray","killedByTeam.green","killedByTeam.light_purple","killedByTeam.red","killedByTeam.white","killedByTeam.yellow","teamkill.aqua","teamkill.black","teamkill.blue","teamkill.dark_aqua","teamkill.dark_blue","teamkill.dark_gray","teamkill.dark_green","teamkill.dark_purple","teamkill.dark_red","teamkill.gold","teamkill.gray","teamkill.green","teamkill.light_purple","teamkill.red","teamkill.white","teamkill.yellow","minecraft.custom:minecraft.leave_game","minecraft.custom:minecraft.play_one_minute","minecraft.custom:minecraft.time_since_death","minecraft.custom:minecraft.time_since_rest","minecraft.custom:minecraft.sneak_time","minecraft.custom:minecraft.walk_one_cm","minecraft.custom:minecraft.crouch_one_cm","minecraft.custom:minecraft.sprint_one_cm","minecraft.custom:minecraft.swim_one_cm","minecraft.custom:minecraft.fall_one_cm","minecraft.custom:minecraft.climb_one_cm","minecraft.custom:minecraft.fly_one_cm","minecraft.custom:minecraft.dive_one_cm","minecraft.custom:minecraft.minecart_one_cm","minecraft.custom:minecraft.boat_one_cm","minecraft.custom:minecraft.pig_one_cm","minecraft.custom:minecraft.horse_one_cm","minecraft.custom:minecraft.aviate_one_cm","minecraft.custom:minecraft.jump","minecraft.custom:minecraft.drop","minecraft.custom:minecraft.damage_dealt","minecraft.custom:minecraft.damage_taken","minecraft.custom:minecraft.deaths","minecraft.custom:minecraft.mob_kills","minecraft.custom:minecraft.animals_bred","minecraft.custom:minecraft.player_kills","minecraft.custom:minecraft.fish_caught","minecraft.custom:minecraft.talked_to_villager","minecraft.custom:minecraft.traded_with_villager","minecraft.custom:minecraft.eat_cake_slice","minecraft.custom:minecraft.fill_cauldron","minecraft.custom:minecraft.use_cauldron","minecraft.custom:minecraft.clean_armor","minecraft.custom:minecraft.clean_banner","minecraft.custom:minecraft.interact_with_brewingstand","minecraft.custom:minecraft.interact_with_beacon","minecraft.custom:minecraft.inspect_dropper","minecraft.custom:minecraft.inspect_hopper","minecraft.custom:minecraft.inspect_dispenser","minecraft.custom:minecraft.play_noteblock","minecraft.custom:minecraft.tune_noteblock","minecraft.custom:minecraft.pot_flower","minecraft.custom:minecraft.trigger_trapped_chest","minecraft.custom:minecraft.open_enderchest","minecraft.custom:minecraft.enchant_item","minecraft.custom:minecraft.play_record","minecraft.custom:minecraft.interact_with_furnace","minecraft.custom:minecraft.interact_with_crafting_table","minecraft.custom:minecraft.open_chest","minecraft.custom:minecraft.sleep_in_bed","minecraft.custom:minecraft.open_shulker_box"}
CRITERIA_BLOCKS = {"minecraft.mined:"}
CRITERIA_ITEMS = {"minecraft.crafted:","minecraft.used:","minecraft.broken:","minecraft.picked_up:","minecraft.dropped:"}
CRITERIA_ENTITIES = {"minecraft.killed:","minecraft.killed_by:"}