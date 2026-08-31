import streamlit as st
import pandas as pd
import random

# Initial 100 Player Dataset
PLAYERS_DATA = [
    {"Name": "Sachin Tendulkar", "Role": "Batsman", "Country": "India", "Average": 53.78, "Economy": 4.1, "Base Price (Cr)": 2.0},
    {"Name": "Virat Kohli", "Role": "Batsman", "Country": "India", "Average": 53.55, "Economy": 5.2, "Base Price (Cr)": 2.0},
    {"Name": "Sir Don Bradman", "Role": "Batsman", "Country": "Australia", "Average": 99.94, "Economy": 0.0, "Base Price (Cr)": 2.0},
    {"Name": "Brian Lara", "Role": "Batsman", "Country": "West Indies", "Average": 52.88, "Economy": 0.0, "Base Price (Cr)": 2.0},
    {"Name": "Viv Richards", "Role": "Batsman", "Country": "West Indies", "Average": 50.23, "Economy": 4.49, "Base Price (Cr)": 2.0},
    {"Name": "Ricky Ponting", "Role": "Batsman", "Country": "Australia", "Average": 51.85, "Economy": 4.16, "Base Price (Cr)": 1.5},
    {"Name": "AB de Villiers", "Role": "Batsman", "Country": "South Africa", "Average": 50.66, "Economy": 5.92, "Base Price (Cr)": 2.0},
    {"Name": "Chris Gayle", "Role": "Batsman", "Country": "West Indies", "Average": 42.19, "Economy": 4.78, "Base Price (Cr)": 1.5},
    {"Name": "Rohit Sharma", "Role": "Batsman", "Country": "India", "Average": 49.12, "Economy": 5.25, "Base Price (Cr)": 1.5},
    {"Name": "Babar Azam", "Role": "Batsman", "Country": "Pakistan", "Average": 47.5, "Economy": 0.0, "Base Price (Cr)": 1.5},
    {"Name": "MS Dhoni", "Role": "WK-Batsman", "Country": "India", "Average": 50.57, "Economy": 5.0, "Base Price (Cr)": 2.0},
    {"Name": "Adam Gilchrist", "Role": "WK-Batsman", "Country": "Australia", "Average": 47.6, "Economy": 4.21, "Base Price (Cr)": 2.0},
    {"Name": "Kumar Sangakkara", "Role": "WK-Batsman", "Country": "Sri Lanka", "Average": 57.4, "Economy": 0.0, "Base Price (Cr)": 2.0},
    {"Name": "Jos Buttler", "Role": "WK-Batsman", "Country": "England", "Average": 41.2, "Economy": 0.0, "Base Price (Cr)": 1.5},
    {"Name": "Jacques Kallis", "Role": "All-Rounder", "Country": "South Africa", "Average": 55.37, "Economy": 3.6, "Base Price (Cr)": 2.0},
    {"Name": "Kapil Dev", "Role": "All-Rounder", "Country": "India", "Average": 31.05, "Economy": 2.78, "Base Price (Cr)": 2.0},
    {"Name": "Imran Khan", "Role": "All-Rounder", "Country": "Pakistan", "Average": 37.69, "Economy": 2.54, "Base Price (Cr)": 2.0},
    {"Name": "Ben Stokes", "Role": "All-Rounder", "Country": "England", "Average": 36.35, "Economy": 4.12, "Base Price (Cr)": 1.5},
    {"Name": "Hardik Pandya", "Role": "All-Rounder", "Country": "India", "Average": 34.2, "Economy": 5.5, "Base Price (Cr)": 1.5},
    {"Name": "Ravindra Jadeja", "Role": "All-Rounder", "Country": "India", "Average": 36.5, "Economy": 4.88, "Base Price (Cr)": 1.5},
    {"Name": "Muttiah Muralitharan", "Role": "Bowler", "Country": "Sri Lanka", "Average": 23.08, "Economy": 2.47, "Base Price (Cr)": 2.0},
    {"Name": "Shane Warne", "Role": "Bowler", "Country": "Australia", "Average": 25.41, "Economy": 2.65, "Base Price (Cr)": 2.0},
    {"Name": "Wasim Akram", "Role": "Bowler", "Country": "Pakistan", "Average": 23.5, "Economy": 3.89, "Base Price (Cr)": 2.0},
    {"Name": "Glenn McGrath", "Role": "Bowler", "Country": "Australia", "Average": 21.64, "Economy": 2.49, "Base Price (Cr)": 2.0},
    {"Name": "Jasprit Bumrah", "Role": "Bowler", "Country": "India", "Average": 20.2, "Economy": 4.65, "Base Price (Cr)": 2.0},
    {"Name": "Dale Steyn", "Role": "Bowler", "Country": "South Africa", "Average": 22.95, "Economy": 3.24, "Base Price (Cr)": 2.0},
    {"Name": "Rashid Khan", "Role": "Bowler", "Country": "Afghanistan", "Average": 18.5, "Economy": 4.2, "Base Price (Cr)": 1.5},
    {"Name": "Sunil Narine", "Role": "All-Rounder", "Country": "West Indies", "Average": 21.5, "Economy": 4.01, "Base Price (Cr)": 1.5},
    {"Name": "Shakib Al Hasan", "Role": "All-Rounder", "Country": "Bangladesh", "Average": 29.4, "Economy": 4.55, "Base Price (Cr)": 1.5},
    {"Name": "Andre Russell", "Role": "All-Rounder", "Country": "West Indies", "Average": 27.2, "Economy": 6.05, "Base Price (Cr)": 1.5},
] + [{"Name": f"Legendary Player {i}", "Role": random.choice(["Batsman", "Bowler", "All-Rounder", "WK-Batsman"]), "Country": random.choice(["India", "Australia", "England", "Pakistan", "South Africa"]), "Average": round(random.uniform(25, 45), 2), "Economy": round(random.uniform(3.5, 6.5), 2), "Base Price (Cr)": round(random.choice([0.5, 1.0, 1.5, 2.0]), 1)} for i in range(1, 71)]

st.set_page_config(page_title="Cricket Auction Simulator", layout="wide")

st.title("🏏 Dynamic Cricket Auction & Squad Strategy Dashboard")

# App State Initialization
if "stage" not in st.session_state:
    st.session_state.stage = "setup"
if "teams" not in st.session_state:
    st.session_state.teams = {}
if "players" not in st.session_state:
    st.session_state.players = pd.DataFrame(PLAYERS_DATA)
if "current_player_idx" not in st.session_state:
    st.session_state.current_player_idx = 0
if "auction_log" not in st.session_state:
    st.session_state.auction_log = []

# --- STAGE 1: SETUP ---
if st.session_state.stage == "setup":
    st.header("⚙️ Step 1: Auction Parameters")
    
    col1, col2 = st.columns(2)
    with col1:
        match_format = st.selectbox("Select Match Format", ["T20", "ODI", "Test"])
        num_teams = st.slider("Number of Franchise Teams", 2, 6, 4)
    with col2:
        st.info(f"**Budget Cap:** 100 Crores per team\n\n**Overseas Restriction:** Max {'6' if match_format == 'T20' else '8'} players per squad.")
        theme_color = st.color_picker("Pick Dashboard Accent Color", "#007A87")

    st.subheader("📝 Step 2: Customize Player Roster (100 Legends)")
    edited_df = st.data_editor(st.session_state.players, num_rows="dynamic", use_container_width=True)
    
    if st.button("🚀 Finalize Roster & Start Auction"):
        st.session_state.players = edited_df
        st.session_state.format = match_format
        st.session_state.num_teams = num_teams
        st.session_state.overseas_cap = 6 if match_format == "T20" else 8
        
        # Initialize Teams
        for i in range(1, num_teams + 1):
            st.session_state.teams[f"Team {i}"] = {
                "budget": 100.0,
                "squad": [],
                "playing_11": []
            }
        st.session_state.stage = "auction"
        st.rerun()

# --- STAGE 2: AUCTION ARENA ---
elif st.session_state.stage == "auction":
    st.header("🔨 Live Bidding Arena")
    
    # Progress & Dashboard Stats
    total_players = len(st.session_state.players)
    idx = st.session_state.current_player_idx
    
    if idx >= total_players:
        st.success("🎉 All players auctioned or skipped!")
        if st.button("Proceed to Strategy Board ➡️"):
            st.session_state.stage = "playing_11"
            st.rerun()
    else:
        current_player = st.session_state.players.iloc[idx]
        
        # Display Current Nominee
        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric(label="Current Draft Nominee", value=current_player["Name"])
            st.write(f"**Role:** {current_player['Role']} | **Origin:** {current_player['Country']}")
            st.write(f"**Career Avg:** {current_player['Average']} | **Econ Rate:** {current_player['Economy']}")
            st.subheader(f"Base Price: {current_player['Base Price (Cr)']} Cr")
        
        with c2:
            st.subheader("Place Winning Bid")
            bidding_team = st.selectbox("Assign Winner to Franchise", list(st.session_state.teams.keys()) + ["Unsold / Skip"])
            
            if bidding_team != "Unsold / Skip":
                final_price = st.number_input("Final Hammer Price (Cr)", min_value=float(current_player["Base Price (Cr)"]), max_value=100.0, value=float(current_player["Base Price (Cr)"]), step=0.1)
                
                # Check limits
                team_data = st.session_state.teams[bidding_team]
                overseas_count = sum(1 for p in team_data["squad"] if p["Country"] != "India")
                is_overseas = current_player["Country"] != "India"
                
                if team_data["budget"] < final_price:
                    st.error("❌ Not enough budget left in franchise account!")
                elif len(team_data["squad"]) >= 15:
                    st.error("❌ Squad roster limit (15) already reached!")
                elif is_overseas and overseas_count >= st.session_state.overseas_cap:
                    st.error("❌ Overseas athlete limits reached for this format!")
                else:
                    if st.button("🔨 Confirm Sold Hammer Strike"):
                        player_entry = current_player.to_dict()
                        player_entry["Sold Price"] = final_price
                        st.session_state.teams[bidding_team]["squad"].append(player_entry)
                        st.session_state.teams[bidding_team]["budget"] -= final_price
                        st.session_state.auction_log.append(f"✅ {current_player['Name']} sold to {bidding_team} for {final_price} Cr")
                        st.session_state.current_player_idx += 1
                        st.rerun()
            else:
                if st.button("⏩ Skip / Unsold"):
                    st.session_state.auction_log.append(f"⚪ {current_player['Name']} passed Unsold")
                    st.session_state.current_player_idx += 1
                    st.rerun()
                    
        # Sidebar Status Table
        st.sidebar.markdown("### 📊 Franchise Ledgers")
        for t_name, t_info in st.session_state.teams.items():
            st.sidebar.write(f"**{t_name}** | Balance: `{round(t_info['budget'], 2)} Cr` | Squad: `{len(t_info['squad'])}/15`")

# --- STAGE 3: PLAYING 11 SELECTOR ---
elif st.session_state.stage == "playing_11":
    st.header("📋 Tactical Board: Lineup Sheet Configuration")
    st.write("Construct your standard optimal active Playing 11 roster mapping from your 15 recruited entities.")
    
    all_ready = True
    for t_name, t_info in st.session_state.teams.items():
        st.subheader(f"🔷 Lineup Sheet: {t_name}")
        squad_names = [p["Name"] for p in t_info["squad"]]
        
        if len(squad_names) < 11:
            st.warning(f"⚠️ {t_name} has only {len(squad_names)} players in their squad. Minimum 11 required to proceed.")
            all_ready = False
            continue
            
        selected_11 = st.multiselect(f"Pick 11 Players for {t_name}", squad_names, default=squad_names[:11] if len(squad_names)>=11 else None, key=f"select_{t_name}")
        st.session_state.teams[t_name]["playing_11"] = [p for p in t_info["squad"] if p["Name"] in selected_11]
        
        if len(selected_11) != 11:
            st.error("❌ Exactly 11 assets must be chosen to field a valid lineup sheet.")
            all_ready = False

    if all_ready:
        if st.button("🏆 Calculate Performance & Balance Verdict"):
            st.session_state.stage = "evaluation"
            st.rerun()

# --- STAGE 4: EVALUATION ---
elif st.session_state.stage == "evaluation":
    st.header("🏆 AI Balance Engine Leaderboard Matrix")
    
    leaderboard = []
    
    for t_name, t_info in st.session_state.teams.items():
        p11 = t_info["playing_11"]
        
        # Balance scoring formula metrics
        bat_avg = sum(p["Average"] for p in p11) / 11
        bowl_econ = sum(p["Economy"] for p in p11 if p["Role"] in ["Bowler", "All-Rounder"]) / (sum(1 for p in p11 if p["Role"] in ["Bowler", "All-Rounder"]) or 1)
        
        roles = [p["Role"] for p in p11]
        wk_count = roles.count("WK-Batsman")
        ar_count = roles.count("All-Rounder")
        bowl_count = roles.count("Bowler")
        bat_count = roles.count("Batsman")
        
        # Penalties and bonuses
        balance_score = (bat_avg * 1.5) - (bowl_econ * 5)
        if wk_count >= 1: balance_score += 15
        else: balance_score -= 30  # High penalty for no WK
        
        if bowl_count + ar_count >= 5: balance_score += 10
        else: balance_score -= 20  # Lacking options
        
        leaderboard.append({
            "Team": t_name,
            "Squad Score": round(max(0, balance_score), 2),
            "Batting Depth Avg": round(bat_avg, 2),
            "Bowling Econ Factor": round(bowl_econ, 2),
            "Composition": f"Batsmen: {bat_count} | Bowlers: {bowl_count} | All-rounders: {ar_count} | WK: {wk_count}"
        })
        
    ld_df = pd.DataFrame(leaderboard).sort_values(by="Squad Score", ascending=False)
    
    st.balloons()
    st.subheader(f"🥇 Winner Confirmed: {ld_df.iloc[0]['Team']} ✨")
    st.dataframe(ld_df, use_container_width=True)
    
    if st.button("🔄 Restart New Session Simulation"):
        st.session_state.clear()
        st.rerun()
