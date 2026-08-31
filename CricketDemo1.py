import os

# Write the Streamlit application code into a file named cricketauctiondemo.py
code_content = """import streamlit as st
import pandas as pd
import math

# Configure page settings
st.set_page_config(page_title="Cricket Auction Simulator", layout="wide")

# 70 Custom Players Dataset Setup
@st.cache_data
def get_initial_players():
    data = [
        ["Morné Morkel", "Bowler", "South Africa", 34.98, 4.61, 1.5],
        ["Shane Watson", "All-Rounder", "Australia", 34.34, 5.79, 2.0],
        ["Glenn McGrath", "Bowler", "Australia", 41.53, 4.43, 2.0],
        ["Kapil Dev", "All-Rounder", "India", 38.34, 3.90, 1.0],
        ["Graeme Smith", "Batsman", "South Africa", 35.36, 4.78, 1.0],
        ["Gary Kirsten", "Batsman", "South Africa", 34.77, 4.22, 1.0],
        ["Younis Khan", "Batsman", "Pakistan", 43.66, 4.39, 1.0],
        ["Gautam Gambhir", "Batsman", "India", 30.89, 3.52, 1.5],
        ["Imran Khan", "All-Rounder", "Pakistan", 28.58, 3.82, 0.5],
        ["Misbah-ul-Haq", "Batsman", "Pakistan", 31.20, 5.11, 0.5],
        ["Inzamam-ul-Haq", "Batsman", "Pakistan", 30.45, 5.69, 1.0],
        ["James Anderson", "Bowler", "England", 41.36, 4.36, 2.0],
        ["David Boon", "Batsman", "Australia", 35.46, 4.03, 1.5],
        ["Nathan Lyon", "Bowler", "Australia", 41.84, 6.10, 0.5],
        ["Mitchell Johnson", "Bowler", "Australia", 41.18, 5.17, 1.0],
        ["Brett Lee", "Bowler", "Australia", 41.80, 5.27, 1.5],
        ["Keith Miller", "All-Rounder", "Australia", 43.71, 4.90, 2.0],
        ["Anil Kumble", "Bowler", "India", 31.62, 4.15, 2.0],
        ["Stuart Broad", "Bowler", "England", 32.68, 6.34, 2.0],
        ["Kevin Pietersen", "Batsman", "England", 42.83, 6.32, 2.0],
        ["Waqar Younis", "Bowler", "Pakistan", 40.13, 4.94, 1.0],
        ["Wasim Akram", "All-Rounder", "Pakistan", 30.72, 4.94, 2.0],
        ["Ravichandran Ashwin", "Bowler", "India", 31.41, 6.18, 1.0],
        ["Ben Stokes", "All-Rounder", "England", 31.71, 4.73, 0.5],
        ["Hardik Pandya", "All-Rounder", "India", 40.77, 4.27, 1.0],
        ["Mark Boucher", "WK-Batsman", "South Africa", 30.27, 5.57, 1.0],
        ["AB de Villiers", "WK-Batsman", "South Africa", 44.71, 5.94, 1.0],
        ["Jos Buttler", "Batsman", "England", 32.44, 6.43, 1.0],
        ["Travis Head", "Batsman", "Australia", 41.74, 6.20, 0.5],
        ["Jonny Bairstow", "WK-Batsman", "England", 39.48, 5.12, 1.0],
        ["Shaun Pollock", "All-Rounder", "South Africa", 36.23, 6.07, 2.0],
        ["Daryll Cullinan", "Batsman", "South Africa", 29.87, 4.01, 0.5],
        ["Mohammed Shami", "Bowler", "India", 33.30, 5.45, 1.0],
        ["Shikhar Dhawan", "Batsman", "India", 39.35, 6.26, 0.5],
        ["Jasprit Bumrah", "Bowler", "India", 33.26, 5.86, 2.0],
        ["Shoaib Akhtar", "All-Rounder", "Pakistan", 40.70, 4.51, 2.0],
        ["Josh Hazlewood", "Bowler", "Australia", 32.74, 4.67, 1.0],
        ["Ravindra Jadeja", "All-Rounder", "India", 32.43, 5.43, 0.5],
        ["Vernon Philander", "Bowler", "South Africa", 41.76, 4.73, 1.5],
        ["Hansie Cronje", "Batsman", "South Africa", 25.06, 4.06, 0.5],
        ["Andrew Flintoff", "All-Rounder", "England", 30.53, 6.27, 1.0],
        ["Kamran Akmal", "WK-Batsman", "Pakistan", 29.36, 4.97, 2.0],
        ["Dinesh Karthik", "WK-Batsman", "India", 31.03, 4.78, 0.5],
        ["Joe Root", "Batsman", "England", 39.43, 4.89, 2.0],
        ["Steve Smith", "Batsman", "Australia", 35.04, 5.50, 1.0],
        ["Shaheen Afridi", "Bowler", "Pakistan", 38.74, 6.38, 1.5],
        ["Quinton de Kock", "WK-Batsman", "South Africa", 43.25, 4.44, 1.5],
        ["MS Dhoni", "WK-Batsman", "India", 44.18, 3.53, 2.0],
        ["Bhuvneshwar Kumar", "Bowler", "India", 38.97, 4.51, 2.0],
        ["Yasir Shah", "Bowler", "Pakistan", 42.90, 4.15, 0.5],
        ["Lance Klusener", "All-Rounder", "South Africa", 37.22, 3.58, 0.5],
        ["Yuvraj Singh", "Batsman", "India", 43.23, 6.46, 0.5],
        ["Axar Patel", "All-Rounder", "India", 36.18, 5.50, 1.5],
        ["Faf du Plessis", "Batsman", "South Africa", 34.14, 4.77, 1.0],
        ["Rishabh Pant", "WK-Batsman", "India", 25.06, 6.08, 1.0],
        ["Ashwell Prince", "Batsman", "South Africa", 31.52, 4.21, 1.5],
        ["Virat Kohli", "Batsman", "India", 44.02, 4.76, 1.5],
        ["Makhaya Ntini", "Bowler", "South Africa", 26.97, 5.35, 1.5],
        ["Javed Miandad", "Batsman", "Pakistan", 27.14, 3.69, 2.0],
        ["Zaheer Abbas", "Batsman", "Pakistan", 43.86, 5.36, 2.0],
        ["Lungi Ngidi", "Bowler", "South Africa", 37.49, 6.05, 0.5],
        ["Marnus Labuschagne", "Batsman", "Australia", 39.72, 5.35, 0.5],
        ["Ollie Robinson", "Bowler", "England", 34.16, 3.67, 1.5],
        ["Babar Azam", "Batsman", "Pakistan", 39.75, 5.43, 1.0],
        ["Brian McMillan", "All-Rounder", "South Africa", 27.72, 4.43, 1.5],
        ["Harry Brook", "Batsman", "England", 43.98, 5.68, 2.0],
        ["Pat Cummins", "Bowler", "Australia", 38.86, 3.98, 0.5],
        ["Allan Donald", "Bowler", "South Africa", 25.00, 4.86, 1.5],
        ["Mohammad Amir", "All-Rounder", "Pakistan", 29.40, 5.01, 1.0],
        ["Hashim Amla", "Batsman", "South Africa", 26.64, 5.32, 0.5]
    ]
    return pd.DataFrame(data, columns=["Name", "Role", "Country", "Average", "Economy", "Base Price (Cr)"])

if "step" not in st.session_state:
    st.session_state.step = "setup"
    st.session_state.players_df = get_initial_players()

# --- STEP 1: SETUP SCREEN ---
if st.session_state.step == "setup":
    st.title("🏏 Cricket Auction Setup Dashboard")
    
    format_type = st.selectbox("Select Match Format:", ["T20", "ODI", "Test"])
    num_teams = st.slider("Select Number of Teams:", 2, 6, 4)
    
    st.write("### Name Your Teams")
    team_names = []
    for i in range(num_teams):
        name = st.text_input(f"Team {i+1} Name:", f"Franchise {chr(65+i)}")
        team_names.append(name)
        
    if st.button("Confirm Settings & Start Auction"):
        st.session_state.format_type = format_type
        st.session_state.team_names = team_names
        st.session_state.overseas_cap = 6 if format_type == "T20" else 8
        st.session_state.teams_data = {
            name: {"budget": 100.0, "squad": [], "overseas_count": 0} for name in team_names
        }
        st.session_state.current_player_idx = 0
        st.session_state.step = "auction"
        st.rerun()

# --- STEP 2: AUCTION ARENA ---
elif st.session_state.step == "auction":
    st.title("🔨 Live Auction Arena")
    
    players = st.session_state.players_df
    idx = st.session_state.current_player_idx
    
    if idx >= len(players):
        st.success("All players auctioned! Moving to Playing 11 Selections.")
        st.session_state.step = "playing11"
        st.rerun()
        
    player = players.iloc[idx]
    base_price = player["Base Price (Cr)"]
    is_overseas = player["Country"] != "India"
    
    if "current_bid" not in st.session_state or st.session_state.get("bid_player_idx") != idx:
        st.session_state.current_bid = 0.0
        st.session_state.highest_bidder = "None"
        st.session_state.bid_player_idx = idx

    col1, col2 = st.columns()
    
    with col1:
        st.metric(label="Current Player", value=player["Name"])
        st.write(f"**Role:** {player['Role']} | **Country:** {player['Country']}")
        st.write(f"**Average:** {player['Average']} | **Economy:** {player['Economy']}")
        st.write(f"**Base Price:** {base_price} Cr")
        
        if st.session_state.current_bid == 0.0:
            min_next_bid = base_price
        else:
            inc_10 = st.session_state.current_bid * 0.10
            inc_50lakhs = 0.50
            min_next_bid = st.session_state.current_bid + max(inc_10, inc_50lakhs)
            
        st.info(f"Minimum Next Allowed Bid: **{min_next_bid:.2f} Cr**")

    with col2:
        st.subheader("Place Team Bid")
        bidding_team = st.selectbox("Select Bidding Team:", st.session_state.team_names)
        team_stats = st.session_state.teams_data[bidding_team]
        
        if st.button("Submit Bid"):
            if team_stats["budget"] < min_next_bid:
                st.error("Insufficient budget remaining to place this bid!")
            elif is_overseas and team_stats["overseas_count"] >= st.session_state.overseas_cap:
                st.error(f"Overseas limit cap of ({st.session_state.overseas_cap}) hit for this team!")
            elif len(team_stats["squad"]) >= 15:
                st.error("Squad maximum roster depth limit (15) already reached!")
            else:
                st.session_state.current_bid = min_next_bid
                st.session_state.highest_bidder = bidding_team
                st.success(f"Bid updated to {min_next_bid:.2f} Cr by {bidding_team}")
                st.rerun()
                
        st.write("---")
        if st.button("🔨 Sell Player (Hammer Down)"):
            if st.session_state.highest_bidder != "None":
                hb = st.session_state.highest_bidder
                final_cost = st.session_state.current_bid
                
                st.session_state.teams_data[hb]["squad"].append({
                    "Name": player["Name"], "Role": player["Role"], 
                    "Country": player["Country"], "Average": player["Average"], 
                    "Economy": player["Economy"], "Cost": final_cost
                })
                st.session_state.teams_data[hb]["budget"] -= final_cost
                if is_overseas:
                    st.session_state.teams_data[hb]["overseas_count"] += 1
                    
                st.toast(f"Sold! {player['Name']} goes to {hb} for {final_cost:.2f} Cr.")
            else:
                st.toast(f"{player['Name']} went Unsold.")
                
            st.session_state.current_player_idx += 1
            st.rerun()

    st.write("### Franchise Budget Tracking Standings")
    sb_cols = st.columns(len(st.session_state.team_names))
