from datetime import date
from typing import Dict, Optional

from aioetherscan.common import check_sort_direction, check_client_type, check_sync_mode
from aioetherscan.modules.base import BaseModule


class Stats(BaseModule):
    """Stats

    https://docs.etherscan.io/api-endpoints/stats-1
    """

    @property
    def _module(self) -> str:
        return 'stats'

    async def eth_supply(self) -> str:
        """Get Total Supply of Ether"""
        return await self._get(action='ethsupply')

    async def eth2_supply(self) -> str:
        """Get Total Supply of Ether"""
        return await self._get(action='ethsupply2')

    async def eth_price(self) -> Dict:
        """Get ETHER LastPrice Price"""
        return await self._get(action='ethprice')

    async def eth_nodes_size(
            self,
            start_date: date, end_date: date,
            client_type: str, sync_mode: str,
            sort: Optional[str] = None
    ) -> Dict:
        """Get Ethereum Nodes Size"""
        return await self._get(
            action='chainsize',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            clienttype=check_client_type(client_type),
            syncmode=check_sync_mode(sync_mode),
            sort=check_sort_direction(sort)
        )

    async def total_nodes_count(self) -> Dict:
        """Get Total Nodes Count"""
        return await self._get(action='nodecount')

    async def daily_network_tx_fee(self, start_date: date, end_date: date, sort: Optional[str] = None) -> Dict:
        """Get Daily Network Transaction Fee"""
        return await self._get(
            action='dailytxnfee',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def daily_new_address_count(self, start_date: date, end_date: date, sort: Optional[str] = None) -> Dict:
        """Get Daily New Address Count """
        return await self._get(
            action='dailynewaddress',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def daily_network_utilization(self, start_date: date, end_date: date, sort: Optional[str] = None) -> Dict:
        """Get Daily Network Utilization"""
        return await self._get(
            action='dailynetutilization',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def daily_average_network_hash_rate(self, start_date: date, end_date: date,
                                              sort: Optional[str] = None) -> Dict:
        """Get Daily Average Network Hash Rate"""
        return await self._get(
            action='dailyavghashrate',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def daily_transaction_count(self, start_date: date, end_date: date, sort: Optional[str] = None) -> Dict:
        """Get Daily Transaction Count"""
        return await self._get(
            action='dailytx',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def daily_average_network_difficulty(self, start_date: date, end_date: date,
                                               sort: Optional[str] = None) -> Dict:
        """Get Daily Average Network Difficulty"""
        return await self._get(
            action='dailyavgnetdifficulty',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def ether_historical_daily_market_cap(self, start_date: date, end_date: date,
                                                sort: Optional[str] = None) -> Dict:
        """Get Ether Historical Daily Market Cap"""
        return await self._get(
            action='ethdailymarketcap',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )

    async def ether_historical_price(self, start_date: date, end_date: date,
                                     sort: Optional[str] = None) -> Dict:
        """Get Ether Historical Price"""
        return await self._get(
            action='ethdailyprice',
            startdate=start_date.isoformat(),
            enddate=end_date.isoformat(),
            sort=check_sort_direction(sort)
        )
