{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reflect Tables into SQLAlchemy ORM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python SQL toolkit and Object Relational Mapper\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['measurement', 'station']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We can view all of the classes that automap found\n",
    "Base.classes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save references to each table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploratory Climate Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29084027240>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZAAAAEHCAYAAACA3BA3AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAAgAElEQVR4nO2dd5gb1bn/v6+0xbsu6wamGRuMDCn0Zkwx5AIh9ABJCOFSUgiXhBBCboBfIAS4CST3AiGUEFqA0IJNJ2BMccG4YxtXbK0b9q639yatpPf3x0i70uxImhnNaGak9/M8frwajc68c+bMec95yznEzBAEQRAEo/icFkAQBEHwJqJABEEQBFOIAhEEQRBMIQpEEARBMIUoEEEQBMEUokAEQRAEU2RVIER0MBGtTvrXQUS/zIdwgiAIgnshI3kgROQHUAPgeGbeAQDt7e2SSCIIglDgVFVVkfqYURPWfwDYklAegiAIQvFiVIFcCuAlOwQRBEEQvIVuExYRlQGoBfA1Zq5PHE82YQWDQcsFFARBEJwhEAgM/K1lwioxUNa3AKxMVh6ZLuZGgsGg62UEvCMn4B1ZRU5rETmtxStyqjFiwvo+xHwlCIIgxNE1AyGiSgBnAPip3oKZGV1dXYjFYmZls5xhw4ahvb3daTGyYqWcPp8PI0aMANGQ2acgCEJO6FIgzNwDYJyRgru6ulBeXo6ysjJTgtlBeXk5hg0b5rQYWbFSznA4jK6uLowcOdKS8gRBEBLYlokei8VcpTyKlbKyMlfNAgVBKByMONEFQRCEJHZ0RvDMpm5MHFGCqw6uhK/ITMWiQARBEEzQH2Oc8e9GNPQqM/zWUAw3HV5cpmJZTNEEZ555ZtZzvvOd76CtrQ1tbW148skns56vPm/37t244oorcpJTEAT7eGt774DyAIC7V3Y4KI0zFL0CiUajhn8zZ86crOfMnDkTo0ePRnt7O5566qms56vP23vvvfHcc88Zlk0QhPxQ22O87yg08mbCGv2PGkvLa7t636zn7NixA5dccgmOPvporFmzBgcccACeeOIJHH/88bj88ssxd+5c/OQnP8FRRx2FX//612hqakJlZSUefPBBTJ06FQ0NDbjxxhuxfft2AMD999+P448/Hvvuuy9qamrwySef4I9//CPGjh2L6upqTJ8+Hffddx98Ph8OPfRQzJs3D3feeSe2bduGk046CaeddhpuvvlmXHbZZWhra0MkEsFvf/tbnHPOOSnnnXzyybj22mtx6aWXYvHixejr68OvfvUrrF69Gn6/H3/4wx9wyimn4IUXXsB7772H3t5ebNu2Deeeey7uuusuS+tZEAQhHQXvAwkGg3jooYcwbdo0XHvttQOj/GHDhmH27NkAgPPPPx8PPPAApkyZghUrVuCmm27C22+/jZtvvhknnngiXnjhBUSjUXR1dQ0pf+XKlVi6dCkmTpyIiy++GG+//TYuuOCCge/vuOMObNy4EQsXLgQARCIRPP/88xg1ahSam5tx+umn4+yzz045r6+vD/X1gwn/TzzxBABg0aJF2Lx5My666CKsWLECALB27VosWLAA5eXlOOaYY3DNNddgv/32s6cyBUEYoLjc5doUvALZb7/9MG3aNADAJZdcgqeffhoA8O1vfxuAkq+ybNkyXHnllQO/CYfDAIAFCxbgscceAwD4/X5UVVUNKf+oo47C5MmTAQAXX3wxFi9enKJA1DAz7r77bnz66afw+XzYvXs3GhoaMt7DkiVLcM011wAApk6diokTJ6K6uhoAMGPGjAG5DjnkEOzcuVMUiCAIeaHgFYiaREb28OHDASj5KlVVVQMzBLPlpfus5pVXXkFTUxPmz5+P0tJSHHrooejr68v4m0wLXpaXlw/87ff7EYlEdEgtCIKQO3lTIHp8Fnawa9cuLFu2DMcddxxef/11TJs2DWvWrBn4ftSoUZg0aRLeeOMNXHjhhWBmrFu3DoceeihmzJiBp556Ctdddx2i0Si6u7sxatSolPJXrlyJ7du3Y//998frr7+eMpMBgJEjR6Kzs3Pgc0dHB8aPH4/S0lIsWLAAO3fu1DwvmenTp2PmzJmYMWMGqqursXPnTgQCAXz++edWVZMgCIJhCj4K6+CDD8ZLL72E6dOno62tDT/60Y+GnPP444/jn//8J0488URMmzYN7777LgDg3nvvxSeffILp06djxowZ+OKLL4b89thjj8Wdd96JE044AZMmTcJ5552X8v3YsWMxbdo0nHDCCbj99tvx3e9+F6tXr8app56KmTNnYurUqUPOu/POO1PK+PGPf4xoNIrp06fj6quvxqOPPpoy8xAEQXACQ1vaapFuS9v29nZNn0E+2bFjx0AkEwD09fVZuhbWJ598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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Design a query to retrieve the last 12 months of precipitation data and plot the results\n",
    "\n",
    "previous = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "\n",
    "# Perform a query to retrieve the data and precipitation scores\n",
    "result = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previous).all()\n",
    "\n",
    "# Save the query results as a Pandas DataFrame and set the index to the date column\n",
    "df = pd.DataFrame(result, columns=['date', 'precipitation'])\n",
    "\n",
    "# Sort the dataframe by date\n",
    "# df = df.sort_values(\"date\")\n",
    "df = df.sort_index()\n",
    "\n",
    "# Use Pandas Plotting with Matplotlib to plot the data\n",
    "df.plot(rot=90)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>precipitation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2021.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.177279</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.461190</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.020000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.130000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6.700000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       precipitation\n",
       "count    2021.000000\n",
       "mean        0.177279\n",
       "std         0.461190\n",
       "min         0.000000\n",
       "25%         0.000000\n",
       "50%         0.020000\n",
       "75%         0.130000\n",
       "max         6.700000"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use Pandas to calcualte the summary statistics for the precipitation data\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(9)]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Design a query to show how many stations are available in this dataset?\n",
    "session.query(func.count(Station.station)).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('USC00519281', 2772),\n",
       " ('USC00519397', 2724),\n",
       " ('USC00513117', 2709),\n",
       " ('USC00519523', 2669),\n",
       " ('USC00516128', 2612),\n",
       " ('USC00514830', 2202),\n",
       " ('USC00511918', 1979),\n",
       " ('USC00517948', 1372),\n",
       " ('USC00518838', 511)]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# What are the most active stations? (i.e. what stations have the most rows)?\n",
    "# List the stations and the counts in descending order.\n",
    "session.query(Measurement.station, func.count(Measurement.station)).\\\n",
    "    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(54.0, 85.0, 71.66378066378067)]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Using the station id from the previous query, calculate the lowest temperature recorded, \n",
    "# highest temperature recorded, and average temperature of the most active station?\n",
    "session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\\\n",
    "    filter(Measurement.station == 'USC00519281').all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x290844b0f60>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Choose the station with the highest number of temperature observations.\n",
    "# Query the last 12 months of temperature observation data for this station and plot the results as a histogram\n",
    "import datetime as dt\n",
    "from pandas.plotting import table\n",
    "previous2 = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "\n",
    "\n",
    "results = session.query(Measurement.tobs).\\\n",
    "filter(Measurement.station == 'USC00519281').\\\n",
    "filter(Measurement.date >= previous2).all()\n",
    "##df = pd.DataFrame(results, columns)\n",
    "\n",
    "\n",
    "\n",
    "df = pd.DataFrame(results, columns=['tobs'])\n",
    "df.plot.hist(bins=12)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(62.0, 69.57142857142857, 74.0)]\n"
     ]
    }
   ],
   "source": [
    "# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' \n",
    "# and return the minimum, average, and maximum temperatures for that range of dates\n",
    "def calculate(start_date, end_date):\n",
    " \n",
    "  ###\n",
    "    \n",
    "    \n",
    "    \n",
    "    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()\n",
    "print(calculate('2012-02-28', '2012-03-05'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "62.0 68.36585365853658 74.0\n"
     ]
    }
   ],
   "source": [
    "# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax \n",
    "# for your trip using the previous year's data for those same dates.\n",
    "import datetime as dt\n",
    "\n",
    "prev_year_start = dt.date(2018, 1, 1) - dt.timedelta(days=365)\n",
    "\n",
    "\n",
    "\n",
    "prev_year_end = dt.date(2018, 1, 7) - dt.timedelta(days=365)\n",
    "\n",
    "min, avg, max = calc_temps(prev_year_start.strftime(\"%Y-%m-%d\"), prev_year_end.strftime(\"%Y-%m-%d\"))[0]\n",
    "\n",
    "\n",
    "print(min, avg, max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ppruc\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:15: UserWarning: Matplotlib is currently using module://ipykernel.pylab.backend_inline, which is a non-GUI backend, so cannot show the figure.\n",
      "  from ipykernel import kernelapp as app\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 288x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the results from your previous query as a bar chart. \n",
    "# Use \"Trip Avg Temp\" as your Title\n",
    "# Use the average temperature for the y value\n",
    "# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=plt.figaspect(2.))\n",
    "xpos = 1\n",
    "yerr = tmax-tmin\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "bar = ax.bar(xpos, tmax, yerr=yerr, alpha=0.5, color='coral', align=\"center\")\n",
    "ax.set(xticks=range(xpos), xticklabels=\"a\", title=\"Trip Avg Temp\", ylabel=\"Temp (F)\")\n",
    "\n",
    "\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('USC00516128', 'MANOA LYON ARBO 785.2, HI US', 21.3331, -157.8025, 152.4, 0.31), ('USC00519281', 'WAIHEE 837.5, HI US', 21.45167, -157.84888999999998, 32.9, 0.25), ('USC00518838', 'UPPER WAHIAWA 874.3, HI US', 21.4992, -158.0111, 306.6, 0.1), ('USC00513117', 'KANEOHE 838.1, HI US', 21.4234, -157.8015, 14.6, 0.060000000000000005), ('USC00511918', 'HONOLULU OBSERVATORY 702.2, HI US', 21.3152, -157.9992, 0.9, 0.0), ('USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 21.5213, -157.8374, 7.0, 0.0), ('USC00517948', 'PEARL CITY, HI US', 21.3934, -157.9751, 11.9, 0.0), ('USC00519397', 'WAIKIKI 717.2, HI US', 21.2716, -157.8168, 3.0, 0.0), ('USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 21.33556, -157.71139, 19.5, 0.0)]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the total amount of rainfall per weather station for your trip dates using the previous year's matching dates.\n",
    "# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation\n",
    "startDate = '2012-01-01'\n",
    "endDate = '2012-01-07'\n",
    "\n",
    "banana = [Station.station, Station.name, Station.latitude, \n",
    "       Station.longitude, Station.elevation, func.sum(Measurement.prcp)]\n",
    "\n",
    "results = session.query(*banana).\\\n",
    "    filter(Measurement.station == Station.station).\\\n",
    "    filter(Measurement.date >= startDate).\\\n",
    "    filter(Measurement.date <= endDate).\\\n",
    "    group_by(Station.name).order_by(func.sum(Measurement.prcp).desc()).all()\n",
    "print(results)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Optional Challenge Assignment"
   ]
  }
 ],
 "metadata": {
  "kernel_info": {
   "name": "python3"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  },
  "nteract": {
   "version": "0.12.3"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
