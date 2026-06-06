import pandas as pd

tools = pd.read_csv("data/tools.csv")
usage = pd.read_csv("data/usage-monthly.csv")

# Ratio básicos por herramienta
tools["activation_rate"] = tools["active_studios_30d"] / tools["studios_installed"]
tools["tickets_per_active_studio"] = tools["support_tickets_30d"] / tools["active_studios_30d"].clip(lower=1)
tools["infra_per_active_studio"] = tools["infra_cost_usd_mo"] / tools["active_studios_30d"].clip(lower=1)

# Vista resumida ordenada por "engagement" (deploys por activo)
summary = tools[[
    "tool_id",
    "name",
    "studios_installed",
    "active_studios_30d",
    "activation_rate",
    "retention_week4_pct",
    "deploys_per_active_studio_mo",
    "tickets_per_active_studio",
    "infra_per_active_studio",
    "csat_1to5"
]].sort_values(by="deploys_per_active_studio_mo", ascending=False)

print(summary.to_string(index=False))

# Extra: última foto mensual desde usage-monthly
last_month = usage["month"].max()
last_month_usage = usage[usage["month"] == last_month]

print("\nLast month snapshot from usage-monthly:")
print(last_month_usage.sort_values(by="active_studios_30d", ascending=False).to_string(index=False))